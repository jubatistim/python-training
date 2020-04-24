from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

import os

SECRET_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

print(SECRET_KEY)

output_file("gmap.html")

map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)

p = gmap(SECRET_KEY, map_options, title="Austin")

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78])
)

p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

show(p)