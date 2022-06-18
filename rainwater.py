import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import chart_studio.tools as tls


def trap_rain_water(heights):
    # two pointer approach
    left = 0
    right = len(heights) - 1
    trapped = [0]*len(heights)

    maxLeft = heights[left]
    maxRight = heights[right]

    water = 0

    while left < right:
        if maxLeft < maxRight:
            left += 1

            if heights[left] < maxLeft:
                water += (maxLeft - heights[left])
                trapped[left] = maxLeft - heights[left]
            else:
                maxLeft = heights[left]
        else:
            right -= 1

            if heights[right] < maxRight:
                water += (maxRight - heights[right])
                trapped[right] = maxRight - heights[right]
            else:
                maxRight = heights[right]

    return water, trapped

# generate Plotly model
def plot_rain_water(heights, trapped):
    fig = go.Figure(data=[
        go.Bar(name='Bars', y=heights, marker_color='rgb(145, 150, 158)'),
        go.Bar(name='Water', y=trapped, marker_color='rgb(162, 228, 250)')
    ])

    fig.update_layout(
        title='Rain Water Model',
        xaxis_title='Index',
        yaxis_title='Rain Water Collected',
        barmode='stack',
        bargap=0,
        margin=dict(
            l=50,
            r=50,
            b=70,
            t=15,
            pad=4
        ),
    )
    fig.update_yaxes(dtick='1')
    fig.update_xaxes(dtick='1')
    fig.layout.title = None

    # export to HTML file, which can later be embedded as IFrame
    fig.write_html("static/rainwatermodel.html")