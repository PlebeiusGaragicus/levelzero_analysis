import os
import pathlib

import streamlit as st

st.set_page_config(
    page_title="PF&R Data",
    layout="wide",
    # initial_sidebar_state="expanded",
    # initial_sidebar_state="collapsed",
)

ASSETS_PATH = pathlib.Path.cwd() / "assets"

st.header(":red[Portland Fire] :blue[Data Analysis]", divider=True)

cols2 = st.columns((1, 1, 1))

with cols2[0]:
    with st.container(border=True):
        # st.markdown("### :green[On-scene wait time]")
        st.markdown("### :red[Fire Crew] :blue[On-scene wait times]")


        st.image(str(ASSETS_PATH / "wait_time_analysis.png"), use_column_width=True)

        st.write("This is a simple web app that allows you to explore the Portland Fire data.")
        st.write("The data is from the Portland Fire and Rescue Department and is available on the Portland Open Data Portal.")

        with st.container(border=True):
            st.page_link("pages/1_⏳_one-scene_wait_time.py", label="Launch", icon="🚀", use_container_width=True)

with cols2[1]:
    with st.container(border=True):
        st.markdown("### :violet[Unit Hour Utilization]")

        st.image(str(ASSETS_PATH / "uhu.png"), use_column_width=True)

        st.write("This is a simple web app that allows you to explore the Portland Fire data.")
        st.write("The data is from the Portland Fire and Rescue Department and is available on the Portland Open Data Portal.")

        with st.container(border=True):
            st.page_link("pages/2_🕥_unit_hour_utilization.py", label="Launch", icon="🚀", use_container_width=True)

with cols2[2]:
    with st.container(border=True):
        st.markdown("### :grey[AMR system levels]")

        st.image(str(ASSETS_PATH / "AMRfire.png"), use_column_width=True)

        st.write("Import Remote CAD data to analyze AMR system levels.")

        with st.container(border=True):
            st.page_link("pages/3_🚑_amr_system_levels.py", label="Launch", icon="🚀", use_container_width=True)
