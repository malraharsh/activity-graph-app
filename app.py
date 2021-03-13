import streamlit as st
from bokeh.models.widgets import ColorPicker
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events


def color_picker():
    selected_color = "#ff4466" 
    color_picker = ColorPicker(color=selected_color, title="Choose color:", width=200)
    color_picker.js_on_change("color", CustomJS(code="""
        document.dispatchEvent(new CustomEvent("COLOR_PICKED", {detail: {pickedColor: cb_obj.color}}))
        """))
    result = streamlit_bokeh_events(
        color_picker,
        events="COLOR_PICKED",
        key="picker",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0)

    if result:
        if "COLOR_PICKED" in result:
            selected_color = result.get("COLOR_PICKED")["pickedColor"]
    return selected_color


st.title("Activity's Graph")

st.sidebar.subheader('Choose color')




bg_color = st.sidebar.color_picker('bg_color', value='#00f900', key=3)
color = st.sidebar.color_picker('color')
line = st.sidebar.color_picker('line')
point = st.sidebar.color_picker('point')

colors = ['#77C957', '#1C1C9A', '#E035B3']
bg_color = color_picker()
st.text(bg_color)
bg_color = bg_color[1:]
color = color[1:]
line = line[1:]
point = point[1:]

l = f"(https://activity-graph.herokuapp.com/graph?username=ashutosh00710&bg_color={bg_color}&color={color}&line={line}&point={point}&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)"
link = f"[![Ashutosh's github activity graph]{l}"
# print(link) 

# st.markdown(link)
st.text(bg_color + ' ' + color)
st.text_area('Copy This Link', value=link)





