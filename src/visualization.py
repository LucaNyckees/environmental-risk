import pandas as pd
import plotly.graph_objects as go

def geo_map(df: pd.DataFrame, var: str, time_point: int) -> None:

    col = f'{var}_{time_point}'

    scl = [0,"rgb(150,0,90)"], [0.125,"rgb(0, 0, 200)"], [0.25,"rgb(0, 25, 255)"],\
          [0.375,"rgb(0, 152, 255)"], [0.5,"rgb(44, 255, 150)"], [0.625,"rgb(151, 255, 0)"],\
          [0.75,"rgb(255, 234, 0)"], [0.875,"rgb(255, 111, 0)"], [1,"rgb(255, 0, 0)"]

    df.dropna(subset=[col], inplace=True)

    fig = go.Figure(data=go.Scattergeo(
        lat = df['lat'],
        lon = df['lon'],
        text = df[col].astype(str),
        marker = dict(
            color = df[f'{var}_0'],
            colorscale = scl,
            reversescale = True,
            opacity = 0.7,
            size = 0.5,
            colorbar = dict(
                outlinecolor = "rgba(68, 68, 68, 0)",
                ticks = "outside",
                showticksuffix = "last",
                dtick = round((df[col].max() - df[col].min()) / 10, 0)
            )
        )
    ))

    # focus point
    lat_foc =46.87775
    lon_foc = 7.4653056

    fig.update_layout(
        title=f'Geo-heat map for {var} at time 0',
        geo = dict(
            projection_scale=10,
            center=dict(lat=lat_foc, lon=lon_foc),
            resolution = 50,
            scope='europe'
        ))

    fig.show()
