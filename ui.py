from task import Story
import streamlit as st 

story = Story()

main_story = story.display_story()

if 'story' not in st.session_state:
    st.session_state['story'] = main_story

st.title('Main Story')


sentence = st.chat_input('Enter your story sentence')
if sentence:
    story.add_sentence(sentence)
    sen = st.session_state.story
    st.session_state.story = sen + ' ' + sentence + '.'
    
    
    st.write(st.session_state.story)

