import netCDF4 as nc
import numpy as np
from netCDF4._netCDF4 import Dataset
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def explore_nc_data(ds: Dataset, var: str) -> None:

    for k in set(ds.variables.keys()) & {'E', 'N', 'time'}:
        print(f"- variable {k} : shape {ds[k].shape}")

    var_shape = ds.variables[var].shape

    print(f"- variable {var} : shape {var_shape}")

    print(f"- data points at each time point : {var_shape[1] * var_shape[2]}")

    return None


def nc_to_pd(ds: Dataset, var: str, rounding: bool) -> pd.DataFrame:

    # var shape : (time_dim, N_dim | chy_dim, E_dim | chx_dim)

    explore_nc_data(ds=ds, var=var)

    keys = set(ds.variables.keys())

    if not {'lat', 'lon', 'E', 'N'} <= keys and not {'lat', 'lon', 'chx', 'chy'} <= keys:
        raise ValueError("Unvalid geo-coordinate system.")
    
    if {'E', 'N'} <= keys:
        geo_var1 = 'E'
        geo_var2 = 'N'
    else:
        geo_var1 = 'chx'
        geo_var2 = 'chy'

    values = ds.variables[var][:].data

    time_dim = ds.variables['time'].shape[0]
    geo_var1_dim = ds.variables[geo_var1].shape[0]
    geo_var2_dim = ds.variables[geo_var2].shape[0]

    longitudes = ds.variables['lon'][:].data.flatten()
    latitudes = ds.variables['lat'][:].data.flatten()

    values_ = values.reshape((time_dim, geo_var1_dim * geo_var2_dim))

    time_series_dict = {f'{var}_{i}': values_[i] for i in range(time_dim)}

    df = pd.DataFrame(time_series_dict | {'lon': longitudes, 'lat': latitudes})

    if rounding:
        for i in range(time_dim):
            df[f'{var}_{i}'] = df[f'{var}_{i}'].round()

    rounded_fill_value = round(ds.variables[var]._FillValue)

    df = df.replace(rounded_fill_value, np.nan)

    return df


def avg_time_series(df: pd.DataFrame, var: str) -> None:

    time_dim = len([k for k in df.keys() if f'{var}_' in k])

    x = list(range(time_dim))
    y_mean = [df[f'{var}_{i}'].mean() for i in x]
    y_max = [df[f'{var}_{i}'].max() for i in x]
    y_min = [df[f'{var}_{i}'].min() for i in x]

    layout = go.Layout(
        title=f'Average time series for {var}',
        xaxis=dict(title='time'),
        yaxis=dict(title=f'aggregate {var}')
    )

    fig = go.Figure(layout=layout)

    for y, mode in zip([y_mean, y_max, y_min], ['avg', 'max', 'min']): 
        scatter_trace = go.Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            name=f'{mode}_{var}'
        )
        fig.add_trace(scatter_trace)

    fig.show()
