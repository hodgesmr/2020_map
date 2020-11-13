import os

import geopandas as gpd 
import matplotlib.pyplot as plt
import pandas as pd

CWD = os.path.dirname(os.path.realpath(__file__))

STATE_SHAPES_DIRECTORY = f'{CWD}/geographies'
STATES_SHAPE_FILES = {state_file[:2]: f'{CWD}/geographies/{state_file}' for state_file in next(os.walk("geographies"))[2]}

fig, ax0 = plt.subplots(figsize=(20, 15))

for state_shape_file in STATES_SHAPE_FILES.values():
    state_df = gpd.read_file(state_shape_file)
    state_df = state_df.to_crs('epsg:32613')

    state_df.plot(ax=ax0, alpha=1, edgecolor='black', linewidth=0.3)

plt.show()
