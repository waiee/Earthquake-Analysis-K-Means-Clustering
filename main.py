import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie


#--- FUNCTIONS ---
st.set_page_config(page_title="waieezainol.com", page_icon=":computer:", layout="wide")
dp_image = Image.open("image/removebgWaiee.png")

# st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">', unsafe_allow_html=True)

# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #00000000;">
#   <a class="navbar-brand" href="#" target="_blank">Waiee Zainol</a> 
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link" href="">Home <span class="sr-only"></span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)


st.markdown("")

#CALL LOTTIE ANIMATION
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- DOWNLOAD PDF ---
def download_pdf():
    with open("image/RESUMEWAIEE.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

    st.download_button(label="Download CV", 
            data=PDFbyte,
            file_name="Waiee_Resume.pdf",
            mime='application/octet-stream')

#--- LOAD ASSET ---
lottie_file = load_lottie("https://assets7.lottiefiles.com/packages/lf20_dlw10cqe.json")

#--- OPEN GITHUB ---
def open_github():
    import webbrowser
    url = 'https://github.com/waiee'
    webbrowser.open_new_tab(url)

#--- INSERT BG URL ---
import base64

#PNG BG
def add_pngbg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: contain;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

#JPG BG
def add_jpgbg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: contain;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

#--- DISPLAY PDF ---
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

#### HORIZONTAL MENU#####
# selected = option_menu(
#         menu_title=None,
#         options=["Home", "Projects", "Contact"],
#         icons=["house", "book", "telephone"],
#         default_index=0, #set homepage
#         orientation="horizontal",
#         styles={      
#             #will add later
#         }
#     )

########################################################################################################
#Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Github", "Contact"],
        icons=["house","github","telephone"],
        default_index=0, #set homepage
    )

# --- HOME ---
if selected == "Home":
    with st.container():
        add_jpgbg('image/gradientwp.jpg')
    # st.title(f"{selected}")
        image_column, right_column = st.columns((1,2))
        with image_column:
            #insert images
                st.image(dp_image, caption="")
        with right_column:
            st.subheader("Hi, I am Waiee :wave:")
            st.title("Bachelor of Computer Science in Data Science")
            st.write("I am passionate in Data Science, Data Analysis, and Machine Learning.")


### WHAT I DO ###
    with st.container():
        st.write("---")
        text_column, image_column = st.columns((2,1))
        with text_column:
            st.header("What I Do")
            st.write("##")
            st.write(
                """
                Welcome!

                I am a 2nd year Computer Science student at Multimedia University Cyberjaya. Love to exchange ideas, meet new people, eager to learn and have heavy discussions. 

                Currently exploring various tech-related fields such as Data Science, Big Data, AI , Machine Learning.

                Let’s grow together! Feel free to get in touch about a new project or opportunity to discuss. Hopefully, we can collaborate and learn together.
                """
            )
            st.write("Check out my [Github]('https://github.com/waiee')")

        with image_column:
            st_lottie(lottie_file, height=400, key="coding")
    
    with st.container():
        # st.write("---")
        add_jpgbg('image/gradientwp.jpg')
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        #Documentation
        contact_form = """
        <form action="https://formsubmit.co/waiee_z@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form> 
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

#--- RESUME ---
# if selected == "Resume":
#     st.header("My Resume")
#     with st.container():
#         add_jpgbg('image/gradientwp.jpg')
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             show_pdf('image/RESUMEWAIEE.pdf')
#         with col2:
#             st.write(' ')
#         with col3:
#             st.write(' ')

# # --- PROJECTS ---
# if selected == "Projects":
#     add_jpgbg('image/gradientwp.jpg')
#     # st.title(f"{selected}")
#     with st.container():
#         # st.write("---")
#         st.header("My Projects")
#         st.write("##")
#         image_column, text_column = st.columns((1,2))
#         # with image_column:
#         #     st_lottie(lottie_file,height=500 ,key="coding")

#         with text_column:
#             st.subheader("This is my first project!")
#             st.write(
#                 """
#                 Learn how to use this streamlit.           
#                 """
#             )
#             st.markdown("[Tutorial Video...]()")
#         #new project section

# --- GITHUB ---
if selected == "Github":
    add_jpgbg('image/gradientwp.jpg')

    import time
    st.success("Redirecting to Github... ")
    with st.spinner("Waiting .."):
        time.sleep(1)
    open_github()
    st.success("Successfull.")
    

# --- CONTACT ---
if selected == "Contact":
    # st.title(f"{selected}")
    with st.container():
        add_jpgbg('image/gradientwp.jpg')
        # st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        #Documentation
        contact_form = """
        <form action="https://formsubmit.co/waiee_z@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form> 
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()