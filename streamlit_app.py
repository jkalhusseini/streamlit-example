import altair as alt
import math
from nbformat import write
import pandas as pd
import streamlit as st
import numpy as np
from scipy.integrate import odeint
from matplotlib import image, pyplot as plt
import plotly.express as px
import random
import time
import numpy as np 
from skimage import io
import plotly.figure_factory as ff


col1, col2 = st.columns(2)

with col1:
    vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
    volume = vol.T
    r, c = volume[0].shape

    # Define frames
    import plotly.graph_objects as go
    nb_frames = 68

    fig = go.Figure(frames=[go.Frame(data=go.Surface(
        z=(6.7 - k * 0.1) * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67 - k]),
        cmin=0, cmax=200
        ),
        name=str(k) # you need to name the frame for the animation to behave properly
        )
        for k in range(nb_frames)])

    # Add data to be displayed before animation starts
    fig.add_trace(go.Surface(
        z=6.7 * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67]),
        colorscale='blues',
        cmin=0, cmax=200,
        colorbar=dict(thickness=20, ticklen=4)
        ))


    def frame_args(duration):
        return {
                "frame": {"duration": duration},
                "mode": "immediate",
                "fromcurrent": True,
                "transition": {"duration": duration, "easing": "linear"},
            }

    sliders = [
                {
                    "pad": {"b": 10, "t": 60},
                    "len": 0.9,
                    "x": 0.1,
                    "y": 0,
                    "steps": [
                        {
                            "args": [[f.name], frame_args(0)],
                            "label": str(k),
                            "method": "animate",
                        }
                        for k, f in enumerate(fig.frames)
                    ],
                }
            ]

    # Layout
    fig.update_layout(
            title='Slices in volumetric data',
            width=600,
            height=600,
            scene=dict(
                        zaxis=dict(range=[-0.1, 6.8], autorange=False),
                        aspectratio=dict(x=1, y=1, z=1),
                        ),
            updatemenus = [
                {
                    "buttons": [
                        {
                            "args": [None, frame_args(50)],
                            "label": "&#9654;", # play symbol
                            "method": "animate",
                        },
                        {
                            "args": [[None], frame_args(0)],
                            "label": "&#9724;", # pause symbol
                            "method": "animate",
                        },
                    ],
                    "direction": "left",
                    "pad": {"r": 10, "t": 70},
                    "type": "buttons",
                    "x": 0.1,
                    "y": 0,
                }
            ],
            sliders=sliders
    )

    fig.show()





data = pd.DataFrame

g0 = random.randint(1,500)
g1 = random.randint(1,500)
g2 = random.randint(1,500)
g3 = random.randint(1,500)
g4 = random.randint(1,500)
g5 = random.randint(1,500)
g6 = random.randint(1,500)
    

c1 = random.randint(1,500)
c2 = random.randint(1,500)


   #Mathematical proportionality components
s = 100
ae = 0.2
Phi_i = 1 
Phi_n = 0.6
n_i = 1
Rp = 1

def model(Rp, g1, c1, c2, g5, g6):
    s = 100
    ae = 0.2
    Phi_i = 1 
    Phi_n = 0.6
    n_i = 1
    Rp = 1
    dRp = (Rp/3)*(((
        c1
    *(g5+g6)-s*g1)*(0.0666666))*(Rp*Rp)+(s*Phi_i)-(s*Phi_n)-((s*2*ae)/Rp)-c1*(n_i)-c2)
    return dRp 

with col2:
    print(g0)
    print(g1)

    if st.button("Generate random parameters"):
        model(Rp, g1, c1, c2, g5, g6)



    

fig = ff.create_scatterplotmatrix(data, diag='histogram', index='Species',
                                  height=800, width=800)

st.write(fig)
        
with col1:
    vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
    volume = vol.T
    r, c = volume[0].shape

    # Define frames
    import plotly.graph_objects as go
    nb_frames = 68

    fig = go.Figure(frames=[go.Frame(data=go.Surface(
        z=(6.7 - k * 0.1) * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67 - k]),
        cmin=0, cmax=200
        ),
        name=str(k) # you need to name the frame for the animation to behave properly
        )
        for k in range(nb_frames)])

    # Add data to be displayed before animation starts
    fig.add_trace(go.Surface(
        z=6.7 * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67]),
        colorscale='blues',
        cmin=0, cmax=200,
        colorbar=dict(thickness=20, ticklen=4)
        ))


    def frame_args(duration):
        return {
                "frame": {"duration": duration},
                "mode": "immediate",
                "fromcurrent": True,
                "transition": {"duration": duration, "easing": "linear"},
            }

    sliders = [
                {
                    "pad": {"b": 10, "t": 60},
                    "len": 0.9,
                    "x": 0.1,
                    "y": 0,
                    "steps": [
                        {
                            "args": [[f.name], frame_args(0)],
                            "label": str(k),
                            "method": "animate",
                        }
                        for k, f in enumerate(fig.frames)
                    ],
                }
            ]

    # Layout
    fig.update_layout(
            title='Slices in volumetric data',
            width=600,
            height=600,
            scene=dict(
                        zaxis=dict(range=[-0.1, 6.8], autorange=False),
                        aspectratio=dict(x=1, y=1, z=1),
                        ),
            updatemenus = [
                {
                    "buttons": [
                        {
                            "args": [None, frame_args(50)],
                            "label": "&#9654;", # play symbol
                            "method": "animate",
                        },
                        {
                            "args": [[None], frame_args(0)],
                            "label": "&#9724;", # pause symbol
                            "method": "animate",
                        },
                    ],
                    "direction": "left",
                    "pad": {"r": 10, "t": 70},
                    "type": "buttons",
                    "x": 0.1,
                    "y": 0,
                }
            ],
            sliders=sliders
    )

    fig.show()

