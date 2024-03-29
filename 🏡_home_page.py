import os
import pathlib

import streamlit as st

st.set_page_config(
    page_title="PF&R Data",
    layout="wide",
    # initial_sidebar_state="expanded",
    initial_sidebar_state="collapsed",
)

ASSETS_PATH = pathlib.Path.cwd() / "assets"

st.header(":red[Portland Fire] :blue[Data Analysis]", divider=True)

cols2 = st.columns((1, 1, 1))

with cols2[0]:
    with st.container(border=True):
        st.markdown("### :green[On-scene wait time]")


        st.image(str(ASSETS_PATH / "wait_time_analysis.png"), use_column_width=True)

        st.write("This is a simple web app that allows you to explore the Portland Fire data.")
        st.write("The data is from the Portland Fire and Rescue Department and is available on the Portland Open Data Portal.")
        st.write("The data is updated daily and includes information on all incidents that the Portland Fire and Rescue Department responds to.")
        st.write("You can explore the data by selecting a specific date range and filtering by incident type, neighborhood, and more.")

        with st.container(border=True):
            st.page_link("pages/1_⏳_one-scene_wait_time.py", label="Launch", icon="🚀", use_container_width=True)

with cols2[1]:
    with st.container(border=True):
        st.markdown("### :violet[Unit Hour Utilization]")

        st.image(str(ASSETS_PATH / "uhu.png"), use_column_width=True)

        st.write("This is a simple web app that allows you to explore the Portland Fire data.")
        st.write("The data is from the Portland Fire and Rescue Department and is available on the Portland Open Data Portal.")
        st.write("The data is updated daily and includes information on all incidents that the Portland Fire and Rescue Department responds to.")
        st.write("You can explore the data by selecting a specific date range and filtering by incident type, neighborhood, and more.")

        with st.container(border=True):
            st.page_link("pages/2_🚑_unit_hour_utilization.py", label="Launch", icon="🚀", use_container_width=True)

with cols2[2]:
    with st.container(border=True):
        st.markdown("### :grey[Placeholder]")

        st.image(str(ASSETS_PATH / "neuromancer_head.png"), use_column_width=True)

        st.write("This is a simple web app that allows you to explore the Portland Fire data.")
        st.write("The data is from the Portland Fire and Rescue Department and is available on the Portland Open Data Portal.")
        st.write("The data is updated daily and includes information on all incidents that the Portland Fire and Rescue Department responds to.")
        st.write("You can explore the data by selecting a specific date range and filtering by incident type, neighborhood, and more.")

        with st.container(border=True):
            st.page_link("pages/2_🚑_unit_hour_utilization.py", label="Launch", icon="🚀", use_container_width=True)




        




DATA_TYPES_AND_COLUMNS = """
## Data Types
Blah blah blah...

## Columns

| Column Name | Description |
| ----------- | ----------- |
| `Activity Type`   | |
|                   | <blank> |
|                   | S - 'signal' |
|                   | M - 'message' |
|                   | C - 'comms (between dispatchers?)' |
| `Apparatus Status` | |
|                   | <blank> |
|                   | DP - 'dispatched' |
|                   | EN - 'enroute' |
|                   | OS - 'on scene' |
|                   | OG - 'staged' |
|                   | TR - 'transporting' |
|                   | TC - 'transport complete' |
|                   | AV - 'available' |
|                   | IQ - 'in quarters' |
|                   | ZZ - 'no status but on board' |
|                   | FF - 'Crew members riding in to hopital with AMR' |
|                   | NA - 'OOS with code' |
| `Activity Code`   | |
|                  | <blank> |
|                  | CM - ??? |
|                  | 7P - 'personnel (AMR lunch break taken at end of shift)' |
|                  | 7C - 'AMR Company Code 1 (aka private transport)' |
|                  | 90 - ?? |
|                  | 91 - ?? |
|                  | 98 - ?? |
|                  | 99 - ?? |

"""

ASSET_FOLDER = os.path.join(os.path.dirname(__file__), "assets")


st.markdown("# Welcome to your personal Data Analysis Suite")
st.write("Select an Analysis method from the sidebar on the left.")

# st.image(os.path.join(ASSET_FOLDER, "pf&r-logo.png"), width=200)

with st.expander("How to export data from 'remote CAD'"):
    image_column, text_column = st.columns ( (1, 2) )

    with image_column:
        st.image("https://picsum.photos/200")
    
    with text_column:
        st.write("This is a column of text")

with st.expander("Explain data types and columns"):
    st.write(DATA_TYPES_AND_COLUMNS)



############## DEBUG TESTING ONLY ##############
if not os.getenv("DEBUG", False):
    st.stop()

st.write("https://www.markdownguide.org/extended-syntax/")
st.write("# Testing purposes only")

st.warning('This is a warning', icon="⚠️")
# with st.spinner('Wait for it...'):
#     time.sleep(5)

import time
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.02)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:') # TODO

