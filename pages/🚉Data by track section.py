import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from functions import importing_data, list_maker
config = {'displayModeBar': False}

st.set_page_config(page_title = "Metro do Porto Dashboard", layout = "wide")

###
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 
          "Setembro", "Outubro", "Novembro", "Dezembro"]
years = ["2018", "2019"]
color_discrete_map = {'Occupancy Rate': 'rgb(0,48,95)'}
df = pd.read_csv(f"Data/Cleaned/2018/Abril/Média 6h-7h.csv")
B_list = []
###

###
def metric_creator(label, value, mode):
	if mode == 0:
		wch_colour_box = (131, 201, 255)
		wch_colour_font = (0,0,0)
	else:
		wch_colour_box = (0, 104, 201)
		wch_colour_font = (255,255,255)	
	fontsize = 26
	valign = "center"
	iconname = "fas fa-asterisk"
	sline = label
	lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
	i = value

	htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 1); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 1); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 16px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
	return htmlstr
###

with st.container(): 
	st.title("🚉 Analysis by track section")
	st.write("Metro do Porto operational indicators for a given corridor for a specific month")
st.write("---")

col1,col2 = st.columns(2)
year = col1.selectbox("Select a year", years)
month = col2.selectbox("Select a month", months)
A = col1.selectbox("Select station A", sorted(df["A"].unique()))

for i in range(len(df[df["A"] == A]["B"])):
    B_list.append(df[df["A"] == A]["B"].iloc[i])

for i in range(len(df[df["B"] == A]["A"])):
    B_list.append(df[df["B"] == A]["A"].iloc[i])

B = col2. selectbox("Select station B", sorted(B_list))
st.write("---")

dataset_list = importing_data(year,month)
occupancy, tramtrains, eurotrams, AtoB, BtoA, PassAtoB, PassBtoA, A, B = list_maker(A, B, dataset_list)

###
col1, col2, col3 = st.columns(3)

df = dataset_list[-1][(dataset_list[-1]["A"] == A) & (dataset_list[-1]["B"] == B)]
    
if df.empty:
    df = dataset_list[-1][(dataset_list[-1]["A"] == B) & (dataset_list[-1]["B"] == A)]

col1.markdown(metric_creator("Monthly average occupancy", "{:.2f}".format(df["OccupancyTotal"].iloc[0] * 100)+ " %", 0) , unsafe_allow_html=True)
col2.markdown(metric_creator("Total number of passagers", str(df["PassagersTotal"].iloc[0]), 1), unsafe_allow_html = True)
col3.markdown(metric_creator("Total number of train movements", str(df["EurotramTotal"].iloc[0] + df["TraintramTotal"].iloc[0]), 0), unsafe_allow_html = True)

###

###
col1, col2 = st.columns(2)

with col1:
	st.subheader("Average vehicle occupancy rate")
	fig = px.bar(pd.DataFrame(data = {"Hour" : [i for i in range(6,24)], "Occupancy Rate" : np.round(np.array(occupancy),4) * 100}),
					x='Hour', y='Occupancy Rate', title = "Vehicle occupancy rate by hour")
	fig.update_traces(hovertemplate=None)
	fig.update_layout(hovermode="x unified")
	st.plotly_chart(fig, use_container_width = True, theme="streamlit", config = config)

with col2:
	st.subheader("Train movements")
	fig = px.bar(pd.DataFrame(data = {"Hour" : [i for i in range(6,24)], "Eurotram" : eurotrams, "Tramtrain": tramtrains}),
					x='Hour', y=["Eurotram", "Tramtrain"], title = "Train movements by type of train")
	fig.update_traces(hovertemplate=None)
	fig.update_layout(hovermode="x unified")
	st.plotly_chart(fig, use_container_width = True, theme = "streamlit", config = config)


col1, col2 = st.columns(2)

with col1:
	st.subheader(f"Vehicle occupancy rate (from {A} to {B})")

	fig = px.bar(pd.DataFrame(data = {"Hour" : [i for i in range(6,24)], "Occupancy Rate" : np.round(np.array(AtoB),4) * 100}),
					x='Hour', y='Occupancy Rate', title = "Vehicle occupancy rate by hour")
	#fig.update_traces(marker_color='rgb(0,48,95)')
	fig.update_traces(hovertemplate=None)
	fig.update_layout(hovermode="x unified")
	st.plotly_chart(fig, use_container_width = True, theme="streamlit", config = config)

with col2:
	st.subheader(f"Vehicle occupancy rate (from {B} to {A})")

	fig = px.bar(pd.DataFrame(data = {"Hour" : [i for i in range(6,24)], "Occupancy Rate" : np.round(np.array(BtoA),4) * 100}),
					x='Hour', y='Occupancy Rate', title = "Vehicle occupancy rate by hour")
	#fig.update_traces(marker_color='rgb(0,48,95)')
	fig.update_traces(hovertemplate=None)
	fig.update_layout(hovermode="x unified")
	st.plotly_chart(fig, use_container_width = True, theme="streamlit", config = config)

