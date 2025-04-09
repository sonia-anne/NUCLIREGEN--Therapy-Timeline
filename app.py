import pandas as pd
import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(page_title="NUCLIREGEN | Therapeutic Timeline", layout="wide")

# Title
st.title("🧬 NUCLIREGEN: Progeria Therapeutic Timeline Dashboard")

# Timeline Data
timeline_data = {
    "Year": [
        2003, 2006, 2010, 2013, 2015, 2017, 2020, 2021, 2023, 2025
    ],
    "Treatment": [
        "Genetic Discovery",
        "Lonafarnib Preclinical",
        "Lonafarnib Phase II",
        "CRISPR (in vitro)",
        "CRISPR (in vivo - mice)",
        "Progerinina Discovery",
        "Lonafarnib FDA Approval",
        "CRISPR Early Human Trials",
        "NUCLIREGEN Prototype",
        "NUCLIREGEN Clinical Breakthrough"
    ],
    "Details": [
        "Identification of LMNA gene mutation linked to progeria.",
        "Initial animal testing on farnesyltransferase inhibitors.",
        "Limited success in extending lifespan in patients.",
        "Successful gene editing in Petri dish models.",
        "Partial nuclear repair in progeric murine models.",
        "Experimental molecule to bind and neutralize progerin.",
        "Approved by FDA, extends life by ~2.5 years.",
        "CRISPR trials encounter immune responses, off-target risks.",
        "First nucleus-targeting nanobot prototype created.",
        "High accuracy in cellular rejuvenation, non-genomic repair."
    ]
}

df_timeline = pd.DataFrame(timeline_data)

# Timeline Plot
fig = px.timeline(
    df_timeline,
    x_start="Year",
    x_end=[year + 0.8 for year in df_timeline["Year"]],
    y="Treatment",
    color="Treatment",
    hover_name="Treatment",
    hover_data={"Details": True, "Year": False},
    title="📅 Advanced Timeline: 20+ Years of Progeria Therapies"
)

fig.update_yaxes(autorange="reversed")
fig.update_layout(
    height=700,
    title_font_size=24,
    showlegend=False,
    margin=dict(l=20, r=20, t=80, b=20),
    plot_bgcolor="#F9F9F9",
)

st.plotly_chart(fig, use_container_width=True)

# Custom CSS
st.markdown("""
<style>
    .stPlotlyChart {
        border: 2px solid #00FFAA;
        border-radius: 12px;
        box-shadow: 0px 0px 20px rgba(0, 255, 170, 0.3);
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)
