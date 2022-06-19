from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="CW Official Website", page_icon=":star:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_zSGy1w.json")
img_contact_form = Image.open("images/CW-1.png")
img_lottie_animation = Image.open("images/CW-12.png")

st.subheader("Hi, I am CW :wave:")
st.title("A coder and youtuber")
st.write("I am a coding youtuber that helps with errors, and more you can think.")
st.write("[Learn More About Python >](https://www.python.org/doc/essays/blurb/)")
st.write("[Learn More About Roblox >](https://en.wikipedia.org/wiki/Roblox)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Youtube channel named Coding Ware I aim to teach people:
            - coding involving Roblox, Python, etc
            - aim to help with errors, more
            
            Interested? Consider subscribing and turning on notifications so you can be notified when a video comes out!
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCmBu7ljWIH3leazQ5YarIQg)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("How to assign a certain team to a player in ROBLOX")
            st.write(
                """
                Learn how to assign a certain team into a roblox game!
                This is used for for example: Higher rank team, etc.
                I will show you how to do it in this tutorial!
                """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=qnJzPEP3CNU)")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_lottie_animation)
                with text_column:
                    st.subheader("Roblox Bedwars Off Topic")
                    st.write(
                        """
                        There is like no explanation for this video..
                        ..except the image.
                        """
                    )
                    st.markdown("[Watch Video...](https://www.youtube.com/watch?v=EKO3HwGQypo)")
            with st.container():
                image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_lottie_animation)
                with text_column:
                    st.subheader("Roblox Bedwars Off Topic 2")
                    st.write(
                        """
                        There is no explanation again..
                        ..its just the second...
                        the image.
                        """
                    )
                    st.markdown("[Watch Video...](https://www.youtube.com/watch?v=gAFOM255b-U&t=129s)")
                with st.container():
                    st.write("---")
                    st.header("Message Me On Roblox")
                    st.write("##")
                    """
                    Message me by: noxefv
                    """
                    st.markdown("[Profile >](https://www.roblox.com/users/2503235667/profile)")

