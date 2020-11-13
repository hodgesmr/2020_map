import os

import geopandas as gpd 
import matplotlib.pyplot as plt
import pandas as pd

BLUE = "#1375B7"
RED = "#C93135"
WHITE = "#F2F4F8"

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

for state, state_shape_file in STATE_SHAPE_FILES.items():
    state_df = gpd.read_file(state_shape_file)
    state_df = state_df.to_crs('esri:102003')
    state_df.plot(ax=ax0, alpha=1, edgecolor=WHITE, color=STATE_COLORS[state], linewidth=1)

plt.show()
