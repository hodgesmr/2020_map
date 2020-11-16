import math
import os

import geopandas as gpd
from matplotlib import colors
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Polygon

BLUE = "#1375B7"
RED = "#C93135"
OFF_WHITE = "#F2F4F8"
WHITE = "#FFFFFF"
BLACK = "#444444"

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

# Fonts
rcParams['font.family'] = "sans-serif"
rcParams['font.sans-serif'] = ['Futura']

# Figure and Axes
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
colorbar_axes = fig.add_axes([0.15, 0.80, 0.70, 0.025], label="color_bar")

# Draw the map
for state, state_shape_file in STATE_SHAPE_FILES.items():
    state_df = gpd.read_file(state_shape_file)
    label_color = WHITE

    if state == 'AK':
        # Plot Alaska with the Alaska Albers Equal Area Conic projection
        state_df = state_df.to_crs('esri:102006')
        alaska = state_df.plot(ax=alaska_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)
        label_x = state_df.geometry.centroid.iloc[0].coords[0][0]
        label_y = state_df.geometry.centroid.iloc[0].coords[0][1]
        alaska_axes.text(
            s=state,
            x=label_x,
            y=label_y,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=12,
            color=label_color,
        )

    elif state == 'HI':
        # Plot Hawaii with the Hawaii Albers Equal Area Conic projection
        state_df = state_df.to_crs('esri:102007')
        hawaii = state_df.plot(ax=hawaii_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)
        label_x = state_df.geometry.centroid.iloc[0].coords[0][0]
        label_y = state_df.geometry.centroid.iloc[0].coords[0][1]
        label_color = BLACK
        hawaii_axes.text(
            s=state,
            x=0,
            y=1000000,  # these coordinates via trial and error
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=12,
            color=label_color,
        )
    else:
        # Plot the Lower 48 with the USA Contiguous Albers Equal Area Conic projection
        state_df = state_df.to_crs('esri:102003')
        lower_48 = state_df.plot(ax=continguous_axes, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)
        label_x = state_df.geometry.centroid.iloc[0].coords[0][0]
        label_y = state_df.geometry.centroid.iloc[0].coords[0][1]

        # Fix the state labels that need fixing; all trial and error
        if state == 'WI':
            label_x = 480000
            label_y = 800000
        elif state == 'MI':
            label_x = 900000
            label_y = 680000
        elif state == 'DC':
            label_x = 1850000
            label_y = 180000
            label_color = BLACK
        elif state == 'MD':
            label_x = 1890000
            label_y = 260000
            label_color = BLACK
        elif state == 'DE':
            label_x = 1870000
            label_color = BLACK
        elif state == 'NJ':
            label_x = 1900000
            label_color = BLACK
        elif state == 'CT':
            label_x = 2030000
            label_y = 630000
            label_color = BLACK
        elif state == 'RI':
            label_x = 2130000
            label_y = 680000
            label_color = BLACK
        elif state == 'MA':
            label_x = 2130000
            label_y = 800000
            label_color = BLACK
        elif state == 'VT':
            label_y = 990000
        elif state == 'NH':
            label_x = 2100000
            label_y = 900000
            label_color = BLACK
        elif state == 'FL':
            label_x = 1390000
        elif state == 'LA':
            label_x = 322000

        # Create NE-02 and ME-02.
        # I like the stripe style 270towin.com uses
        elif state == 'NE' or state == 'ME':
            #Create a polygon through the state shape

            # Build the left edge of the polygon
            # Find the midpoint, and then scoot a bit to the left
            x1 = ((float(state_df.geometry.bounds.minx.iloc[0]) + float(state_df.geometry.bounds.maxx.iloc[0])) / 2) - 150000
            # Find the highest point in the geometry
            y1 = math.ceil(state_df.geometry.bounds.maxy.iloc[0])
            # Scoot the bottom of the polygon a bit to the right
            x2 = float(x1) + 200000
            # Find the lower point in the geometry
            y2 = math.floor(state_df.geometry.bounds.miny.iloc[0])

            # Build the right edge of the polygon by just creating width
            x3 = x1 + 100000
            y3 = y1
            x4 = x2 + 100000
            y4 = y2
            
            # Convert the polygon to a GeoSeries
            stripe_geo = gpd.GeoSeries(Polygon([[x1, y1], [x2, y2], [x4, y4], [x3, y3]]))
            # Convert the GeoSeries to a GeoDataFrame and match the projection
            stripe_df = gpd.GeoDataFrame(geometry=stripe_geo, crs=state_df.crs)

            #Finally, find the intersection of the GeoDataFrame and the state
            stripe_df = gpd.overlay(stripe_df, state_df,  how='intersection')
            
            # Add it to the map
            if state == 'ME':
                me_02 = stripe_df.plot(ax=continguous_axes, alpha=1, color=RED, linewidth=0)
            elif state == 'NE':
                
                ne_02 = stripe_df.plot(ax=continguous_axes, alpha=1, color=BLUE, linewidth=0)

        # Draw all the state labels
        continguous_axes.text(
            s=state,
            x=label_x,
            y=label_y,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=12,
            color=label_color,
        )

# Draw the colorbar
cmap = colors.ListedColormap([BLUE, RED])
bounds=[0, 306, 538]
norm = colors.BoundaryNorm(bounds, cmap.N)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
colorbar = fig.colorbar(sm, cax=colorbar_axes, ticks=[269], spacing='proportional', drawedges=False, orientation='horizontal')
colorbar.outline.set_visible(False)
colorbar_axes.set_xticklabels([''])
colorbar_axes.xaxis.set_tick_params(length=20, direction="in", colors=BLACK)
colorbar_axes.xaxis.set_ticks_position('top')

# Annotate the colorbar
colorbar_axes.annotate(
    "306",
    xy=(0, 1),
    xytext=(0, 70),
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=40,
    fontweight='semibold',
    color=BLUE,
    textcoords='offset points',
    xycoords='axes fraction',
)

colorbar_axes.annotate(
    "Joseph R. Biden Jr.",
    xy=(0, 1),
    xytext=(0, 34),
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=16,
    fontweight='regular',
    color=BLUE,
    textcoords='offset points',
    xycoords='axes fraction',
)

colorbar_axes.annotate(
    "Kamala D. Harris",
    xy=(0, 1),
    xytext=(0, 16),
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=16,
    fontweight='regular',
    color=BLUE,
    textcoords='offset points',
    xycoords='axes fraction',
)

colorbar_axes.annotate(
    "232",
    xy=(1, 1),
    xytext=(0, 70),
    horizontalalignment='right',
    verticalalignment='top',
    fontsize=40,
    fontweight='semibold',
    color=RED,
    textcoords='offset points',
    xycoords='axes fraction',
)

colorbar_axes.annotate(
    "Donald J. Trump",
    xy=(1, 1),
    xytext=(0, 34),
    horizontalalignment='right',
    verticalalignment='top',
    fontsize=16,
    fontweight='regular',
    color=RED,
    textcoords='offset points',
    xycoords='axes fraction',
)

colorbar_axes.annotate(
    "Michael R. Pence",
    xy=(1, 1),
    xytext=(0, 16),
    horizontalalignment='right',
    verticalalignment='top',
    fontsize=16,
    fontweight='regular',
    color=RED,
    textcoords='offset points',
    xycoords='axes fraction',
)


plt.show()
