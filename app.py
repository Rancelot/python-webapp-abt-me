from PIL import Image
import requests
import streamlit as st 
from streamlit_lottie import st_lottie 


# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Who is Rafael?", page_icon=":thinking_face:", layout="wide")

# ---- LOAD ASSETS ----
lottie_coding_asset = "https://lottie.host/44c52eec-5f86-4730-9081-a1de1ea0f5fa/HLiCTm4gEu.json"
img_tech_desk = Image.open("images/pexels-christina-morillo-1181675.jpg")
img_tech_box = Image.open("images/pexels-cottonbro-studio-4705635.jpg")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Rafael :wave:")
    st.title("A Software Developer From Canada")
    st.write("I am passionate about learning different tech stacks and being able to apply them in functional applications I work on.")
    st.write("[Learn More >](https://www.rpucut.tech/)")
    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write('''
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris lobortis augue et neque rhoncus, eu vulputate purus rhoncus. 
                 Nunc molestie bibendum condimentum. Suspendisse ut luctus erat. Morbi at commodo dolor. Suspendisse at sem et felis aliquam semper. 
                 Integer eleifend hendrerit fermentum. Nulla maximus leo metus, ornare lobortis enim dapibus eget. Fusce ut iaculis dui, at fringilla risus. 
                 Aliquam dignissim nisl sapien, et dapibus tellus maximus sed. Quisque est mi, hendrerit in felis id, scelerisque semper libero.
                 ''')
        st.write("[Find Me Here >](https://ca.linkedin.com/in/rafael-angelo-pucut)")
        
        # want to add an animation? use a LottieFile, a JSON based animation file format
        # small files that work on any device and can scale up or down without any pixelation
    with right_column:
        st_lottie(lottie_coding_asset, height=300, key="codingAnimation")

#  ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_tech_desk)
    with text_column:
        st.subheader("Project 01: Subheader inside the Projects Section of Website")
        st.write("""
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                 """)
        st.markdown("[Watch a Video Here...](https://youtu.be/8H0QjUAnVQk?si=FirtCNMk5Dki9r6p)")
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_tech_box)
    with text_column:
        st.subheader("Project 02: Subheader inside the Projects Section of Website")
        st.write("""
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                 """)
        st.markdown("[Watch a Video Here...](https://youtu.be/uZFROsvADpo?si=RBUogksiKPJ_xuDa)")
        

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    #using https://formsubmit.co/ form functionality
    contact_form_html_inject = """
        <form action="https://formsubmit.co/rpucut@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form_html_inject, unsafe_allow_html=True)
    with right_column:
        st.empty()
        # st.write("Copyright 2023")
    
    
    