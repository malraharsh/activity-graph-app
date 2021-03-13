import streamlit as st

st.title("Github Activity Graph")

username = st.text_input('Enter your github username:')

if username == "":
    st.stop()

st.sidebar.subheader('Choose Colors ->')
bg_color = st.sidebar.color_picker('# Background Color', value='#FBD698')
color = st.sidebar.color_picker('# Color', value='#E26B74')
line = st.sidebar.color_picker('# Line', value='#34FBEA')
point = st.sidebar.color_picker('# Point', value='#AC1CE0')

# colors = ['#77C957', '#1C1C9A', '#E035B3']
# bg_color = st.sidebar.selectbox('bg', colors)

bg_color = bg_color[1:]
color = color[1:] 
line = line[1:]
point = point[1:]


link = f"[![](https://activity-graph.herokuapp.com/graph?username={username}&bg_color={bg_color}&color={color}&line={line}&point={point}&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)"

st.markdown(link)

st.text_area('Copy This Link', value=link)

