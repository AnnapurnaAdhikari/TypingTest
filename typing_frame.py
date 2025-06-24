import streamlit as st
import random
import time

texts = [
    "Life is a daily training ground, and we are each composed of the very actions we take in life.",
    "If you live carelessly, your mind will be soiled, but if you try to live conscientiously, it will slowly become pure again.", 
    "If your heart is pure, the world looks brighter.", " If your world is bright, you can be kinder to others.",
    "The Zen sect of Buddhism is renowned for the cleaning practices of its monks, but cleaning is greatly valued in Japanese Buddhism in general as a way to cultivate the mind.",
    "In this book, I introduce everyday cleaning methods typically employed in temples, while sharing what it's like to be a monk in training.",
   "Regarding Zen practices, I include information gleaned from discussions with Shoyo Yoshimura, a Soto Zen monk who promotes Zen vegetarian cuisine, and an unsui monk (Zen apprentice), Seigaku, who promotes Japanese Zen in Berlin, Germany.",
    "I hope you enjoy applying the cleaning techniques introduced here in your home.", 
    "There's nothing complicated about them. All you need is a will to sweep the dust off your heart."
]

if 'start_time' not in st.session_state:
    st.session_state.start_time = None

st.title("Typing Speed Test")

if st.button("Start New Test"):
    st.session_state.sample_text = random.choice(texts)
    st.session_state.user_input = ""
    st.session_state.start_time = time.time()


if 'sample_text' in st.session_state:
    st.write("Type the folowing text!")
    st.write(f"**{st.session_state.sample_text}**")
    st.session_state.user_input = st.text_area("Start typing here...", value=st.session_state.user_input)

    if st.button("Submit"):
        end_time = time.time()
        time_taken = end_time - st.session_state.start_time
        original = st.session_state.sample_text
        typed = st.session_state.user_input

        words = len(original.split())
        wpm = round((words/time_taken)*60, 2)

        correct_chars = sum(1 for a, b in zip(original, typed) if a == b)
        accuracy = round((correct_chars/len(original)) * 100, 2)

        st.success(f"Results:")
        st.write(f"Time Taken: {round(time_taken, 2)} seconds")
        st.write(f"WPM: {wpm}")
        st.write(f"Accuracy: {accuracy}%")