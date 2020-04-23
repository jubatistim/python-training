from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Make string columns for tooltips
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Bokeh structure for plotting
cds=ColumnDataSource(df)

# Configure x and y axis
p=figure(x_axis_type='datetime',height=100, width=500, sizing_mode = "scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color=None

# Hover tooltips
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

# Plot quadrants
q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

# Output to file
output_file("Graph1.html")
show(p)