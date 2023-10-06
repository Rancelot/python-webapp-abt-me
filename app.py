import streamlit as st 

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Who is Rafael?", page_icon=":thinking_face:", layout="wide")

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
        pass
        # use a lottie file here