import pandas as pd
import streamlit as st
from dtale.views import startup
from dtale.app import get_instance


CSS = """
<style>
    div.sidebar-content {
      padding: 1rem !important;
    }
    section.main div.block-container {
      padding: 3rem 3rem 3rem !important;
    }
    div.block-container > div:first-child {
      height: 100%;
    }
    div.block-container > div > div.element-container:first-child,
    div.block-container > div > div.element-container:last-child {
      height: 100%;
      margin: 0;
    }
    div.block-container > div > div.element-container:nth-child(2) {
      margin: 0;
      margin: 0.5rem 0 0.5rem;
    }
    div.block-container div.markdown-text-container {
      height: 100%;
    }
    div.sidebar-content {
      width: 40rem !important;
    }
    div.sidebar-content pre {
      font-size: 10px;
    }
    div.Widget.row-widget.stRadio > div{
      flex-direction:row;
    }
    div.stBlock-horiz div.stBlock:first-child {
      margin-top: auto;
      margin-bottom: auto;
    }
    div.stBlock-horiz div.stBlock:first-child > div {
      margin-top: 1em;
    }
</style> 
"""





with st.sidebar.header('Upload your csv file'):
    df = st.sidebar.file_uploader('Upload your csv file', type=['csv'])

    dfst = pd.read_csv(df)
    
startup(data_id="1", data=dfst)
dfs = get_instance("1").data


html = f"""
{CSS}
<iframe src="/dtale/main/1" style="height: 100%;width: 125%
"/>
"""
st.markdown(html, unsafe_allow_html=True)
