import os

import geopandas as gpd
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

BLUE = "#1375B7"
RED = "#C93135"
OFF_WHITE = "#F2F4F8"
WHITE = "#FFFFFF"
BLACK = "#000000"

CWD = os.path.dirname(os.path.realpath(__file__))

STATE_SHAPE_FILES = {state_file[:2]: f'{CWD}/geographies/{state_file}' for state_file in next(os.walk("geographies"))[2]}

STATE_COLORS = {
    'AK': RED,
    'AL': RED,
    'AR': RED,
    'AZ': BLUE,
    'CA': BLUE,
    'CO': BLUE,
    'CT': BLUE,
    'DC': BLUE,
    'DE': BLUE,
    'FL': RED,
    'GA': BLUE,
    'HI': BLUE,
    'IA': RED,
    'ID': RED,
    'IL': BLUE,
    'IN': RED,
    'KS': RED,
    'KY': RED,
    'LA': RED,
    'MA': BLUE,
    'MD': BLUE,
    'ME': BLUE,
    'MI': BLUE,
    'MN': BLUE,
    'MO': RED,
    'MS': RED,
    'MT': RED,
    'NC': RED,
    'ND': RED,
    'NE': RED,
    'NH': BLUE,
    'NJ': BLUE,
    'NM': BLUE,
    'NV': BLUE,
    'NY': BLUE,
    'OH': RED,
    'OK': RED,
    'OR': BLUE,
    'PA': BLUE,
    'RI': BLUE,
    'SC': RED,
    'SD': RED,
    'TN': RED,
    'TX': RED,
    'UT': RED,
    'VA': BLUE,
    'VT': BLUE,
    'WA': BLUE,
    'WI': BLUE,
    'WV': RED,
    'WY': RED,
}

fig, ax0 = plt.subplots(figsize=(20, 15))
ax0.set_axis_off()
ax0.axis('equal')
continguous_axes = fig.add_axes([0, 0, 1, 0.8], label="contiguous")
continguous_axes.set_axis_off()
continguous_axes.axis('equal')
hawaii_axes = fig.add_axes([0, -0.05, 0.4, 0.4], label="hawaii")
hawaii_axes.set_axis_off()
hawaii_axes.axis('equal')
alaska_axes = fig.add_axes([0.05, -0.05, 0.25, 0.25], label="alaska")
alaska_axes.set_axis_off()
alaska_axes.axis('equal')
colorbar_axes = fig.add_axes([0.15, 0.82, 0.70, 0.025], label="color_bar")

# Draw the map
for state, state_shape_file in STATE_SHAPE_FILES.items():
    state_df = gpd.read_file(state_shape_file) 
    # Plot Alaska with the Alaska Albers Equal Area Conic projection
    if state == 'AK':
        state_df = state_df.to_crs('esri:102006')
        hawaii = state_df.plot(ax=alaska_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)
    # Plot Hawaii with the Hawaii Albers Equal Area Conic projection
    elif state == "HI":
        state_df = state_df.to_crs('esri:102007')
        alaska = state_df.plot(ax=hawaii_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)
    else:
        # Plot the Lower 48 with the USA Contiguous Albers Equal Area Conic projection
        state_df = state_df.to_crs('esri:102003')
        lower_48 = state_df.plot(ax=continguous_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)

# Draw the colorbar
cmap = colors.ListedColormap([BLUE, RED])
bounds=[0, 306, 538]
norm = colors.BoundaryNorm(bounds, cmap.N)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
colorbar = fig.colorbar(sm, cax=colorbar_axes, ticks=[269], spacing='proportional', drawedges=False, orientation='horizontal')
colorbar.ax.set_xticklabels([''])
colorbar.ax.xaxis.set_tick_params(length=20, direction="in", colors=BLACK)
colorbar.ax.xaxis.set_ticks_position('top')
colorbar.outline.set_visible(False)

plt.show()
