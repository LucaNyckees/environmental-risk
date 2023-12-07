import netCDF4 as nc
from netCDF4._netCDF4 import Dataset
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def explore_nc_data(ds: Dataset) -> None:

    for k in ds.variables.keys():
        print(f"    variable {k} has shape {ds[k][:].data.shape}")

    return None
