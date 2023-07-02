import streamlit as st

# Text title
st.title("Testing Streamlit")

#Header/subHeader
st.header("This is header")
st.subheader("This is a subheader")

#Text
st.text("Hello world")

#Markdown
st.markdown("### This is a markdown")

#Error/colourful text
st.success("Successful!")
#information
st.info("Information")
#warning
st.warning("This is a warning.")
#error
st.error("This is a n error!")
#exception
st.exception("NameError(name three not defined)")

#Get help info about python
st.help(range)

#writing text
st.write("Text with write")
st.write(range(10))

#Images
from PIL import Image
img = Image.open("IMG_4825.jpeg")
st.image(img, width=300, caption="Inilah muka saya")

#Videos
vid_file = open("video.mp4","rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
# audio_file = open("","rb").read()
# st.audio(audio_file,format='audio/mp3')

#Widget
#Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

#Radio Buttons
status = st.radio("What is your status",("Active", "Inactive"))

if status == 'Active':
    st.success("You are Active!")
else:
    st.warning("You are inactive.")

#selectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "Doctor", "Pilot"])
st.write("You selected this option: ", occupation)
#Multiselect
location = st.multiselect("Where do you work?",("London", "New York", "Kelantan", "Keyel"))
st.write("You selected", len(location),"locations")

#Slider
level = st.slider("What is you level",1,10)

# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is fucking cool.")

#Text input
firstname = st.text_input("Enter your firstname","Type Here..")
# if st.button("Submit"):
#     result = firstname.title()
#     st.success(result)

#Text Area
message = st.text_area("Enter your message","Type Here..")
submit = st.button("Submit")
if submit:
    result = message.title()
    st.success(result)

#Date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

#Time 
the_time = st.time_input("The time is", datetime.time())

#Displaying JSON
st.text("Displaying JSON")
st.json({'Name':"Waiee",'Gender':"Male"})

#Display RAW code
st.text("Display Raw Code")
st.code("import numpy as np")

#Display raw code
with st.echo():
    #This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

#Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

#Spinner
with st.spinner("Waiting .."):
    time.sleep(5)
st.success("Finished!")

#Balloons 
# st.balloons()

#SIDEBARS
st.sidebar.header("About Me")
st.sidebar.header("Contact")
st.sidebar.text("Instagram: waiee.z")

#Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())\

# #Plot 
# st.pyplot()

# #Dataframes
# st.dataframe(df)

# #Tables
# st.table(df)