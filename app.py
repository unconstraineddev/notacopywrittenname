import json
import pathlib
from pathlib import Path
import zipfile

import streamlit as st
from pollination_streamlit.selectors import job_selector
from streamlit_vtkjs import st_vtkjs
from honeybee.model import Model

import honeybee_vtk.model
from honeybee_vtk.model import DisplayMode


st.set_page_config(
    page_title='UD Shoebox Study App',
    layout='centered',
    page_icon='assets/UDLogo.png'
)

st.sidebar.image('./assets/UDLogo.png')


def add_viewer(model_vtk):
    return st_vtkjs(
        content=model_vtk, key="viewer"
    )


model = Model.from_hbjson('./model_json/lilkoda.hbjson')
model_vtk = honeybee_vtk.model.Model.from_hbjson(
    model.to_hbjson('temp\\temphbjson', '.', 3))

model_vtk.to_vtkjs(folder='temp', config=None, model_display_mode=DisplayMode.Shaded)

add_viewer(Path('temp\model.vtkjs').read_bytes())
