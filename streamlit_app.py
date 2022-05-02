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
import pandas as pd
from IPython.display import display
from PIL import Image

#Page Title
st.title("Modeling Tumor Growth and the Impact of Nanoparticle-Emitters in Adjuvant Radiotherapy")

#ODE Title
st.subheader("Tumor Model ODE:")

#ODE Image
image = Image.open('Screen Shot 2022-05-01 at 3.11.50 PM.png')
st.image(image, caption = "ODE for outer tumor radius with respect to uniform growth condition.") 

#Mathematical proportionality components
s = 100
ae = 0.2
Phi_i = 1 
Phi_n = 0.6
n_i = 1
Rp = 1

#Defining solvable ODE
def model(Rp, g1, c1, c2, g5, g6):
    """
    def model takes Rp, g1, c1, c2, g5, and g6 as parameters, and calculates dRp (change in tumor growth rate)
    Rp(int): proliferative radius
    g1(int): nutrient supply degradation
    c1(int): Auger effect
    c2(int): Radiotherapy factor
    g5(int): Rate of nanoparticle binding
    g6(int): Rate of nanoparticle degradation
    """
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

#Empty list of lists to be populated with random parameter values
lol = []

#Sidebar initiation
with st.sidebar:

    #Logo image
    image2 = Image.open('cosmos-atom-logo.png')
    st.image(image2, width= 150)

    #Run simulation subhead
    st.subheader("Run Simulation:")

    #Button initiation
    if st.button("Generate random parameters"):
        
        #Generation of 100 random values for each parameter
        for i in range (100):
            g0 = random.randint(1,5000)
            g1 = random.randint(1,5000)
            g2 = random.randint(1,5000)
            g3 = random.randint(1,5000)
            g4 = random.randint(1,5000)
            g5 = random.randint(1,5000)
            g6 = random.randint(1,5000)
            c1 = random.randint(1,5000)
            c2 = random.randint(1,5000)

            #Call to ODE
            model_output = model(Rp, g1, c1, c2, g5, g6)

            #Appending generated values to empty list (lol)
            lol.append([ g5, g6, c1, c2, model_output])

            #Function to convert datagrame to .csv
            def convert_df(df):
                """
                def convert_df converts pandas dataframe to a csv file
                df: pandas dataframe 
                """
                return df.to_csv().encode('utf-8')
            
            #Converting lol into pd.DataFrame
            data = pd.DataFrame(lol)
            csv = convert_df(data)

            #Renaming columns of df
            data.columns= ['Inhibitor Degeneration', 
                "NP Binding", "Auger Effect", "Radiotherapy Factor", "Growth rate"]

    #Presents empty variables when simulation not yet run
    else:
        with st.sidebar:
            st.header("Clinical parameters:")
            st.write("Rate of nutrient consumption:")
            st.write("Nutrient supply degradation:")
            st.write("External inhibitor degradation:")
            st.write("Inhibitor generation by tumor:")
            st.write("Inhibitor degeneration by tumor:")
            st.write("Rate of nanoparticle binding:")
            st.write("Rate of nanoparticle degradation:")
            st.write("Auger effect")
            st.write("Radiotherapy factor:")
            st.write("Output:")
        
    with st.sidebar:
        st.header("Clinical parameters:")
        st.write("Rate of nutrient consumption:",g0)
        st.write("Nutrient supply degradation:", g1)
        st.write("External inhibitor degradation:", g2)
        st.write("Inhibitor generation by tumor:", g3)
        st.write("Inhibitor degeneration by tumor:", g4)
        st.write("Rate of nanoparticle binding:", g5)
        st.write("Rate of nanoparticle degradation:", g6)
        st.write("Auger effect", c1)
        st.write("Radiotherapy factor:", c2)
        st.header("Growth rate:")
        st.write("Output:", model_output)

        #Download button for .csv of output data
        st.download_button(label = "Click to download dataset (.CSV)",
        file_name= "Dataset.csv", data=csv, mime = "text/csv")

st.subheader("Scatterplot Matrix Comparing Individual Parameters:")

#Figure call for scatterplot matrix
fig1 = ff.create_scatterplotmatrix(data, diag='histogram', title= "",
                                  height=800, width=900)
#Streamlit write figure
st.write(fig1)


#Subheader for MRI volumes
st.subheader("Volumetric MRI Voxels:")

vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
volume = vol.T
r, c = volume[0].shape

# Define frames
import plotly.graph_objects as go
nb_frames = 60

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
    """
    def frame_args takes duration as a parameter and controls the time interval for the MRI cross section
    duration(int): slides/sec
    """
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
        title='',
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

st.write(fig)