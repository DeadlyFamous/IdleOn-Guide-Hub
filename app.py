import streamlit as st
from st_click_detector import click_detector

# --- PAGE SETUP ---
st.set_page_config(layout="wide", page_title="Idleon Resource Hub")
st.title("Idleon Guide HUB")

# --- DATA LOADING ---
# This pulls everything from your secrets.toml automatically
RESOURCES = st.secrets["resources"]

# --- TILE GRID ---
content = ""
for item in RESOURCES:
    content += f"""
        <a href='#' id='{item["id"]}' style='margin: 10px; text-decoration: none; display: inline-block;'>
            <div style="text-align: center;">
                <img src='{item["tile_image"]}' 
                     style='width: 150px; height: 150px; object-fit: cover; 
                            border-radius: 10px; border: 2px solid #555; background-color: #2a2a2a;'>
                <p style='color: white; margin-top: 5px; font-weight: bold;'>{item["title"]}</p>
            </div>
        </a>
    """

clicked = click_detector(f"<div style='display: flex; flex-wrap: wrap; justify-content: center;'>{content}</div>")

# --- DISPLAY LOGIC ---
if clicked:
    # Find the specific resource that was clicked
    res = next((item for item in RESOURCES if item["id"] == clicked), None)
    
    if res:
        st.divider()
        col1, col2 = st.columns([0.7, 0.3])
        
        with col1:
            st.subheader(res["title"])
            st.image(res["guide_image"], width="stretch")
            
        with col2:
            st.write("### Quick Links")
            for link in res["links"]:
                st.link_button(link["label"], link["url"], width="stretch")