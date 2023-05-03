import streamlit as st
import pandas as pd
import numpy as np
from functions import importing_data, average_passager, average_occupancy
st.set_page_config(page_title = "Metro do Porto Dashboard", layout = "wide")

###
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 
          "Setembro", "Outubro", "Novembro", "Dezembro"]
years = ["2018", "2019"]
color_discrete_map = {'Occupancy Rate': 'rgb(0,48,95)'}
df = pd.read_csv(f"Data/Cleaned/2018/Abril/Média 6h-7h.csv")
B_list = []
###

with st.container(): 
	st.title("🥇Top 10s")
	st.write("Top ten track sections for various metrics")

col1,col2 = st.columns(2)
year = col1.selectbox("Select a year", years)
month = col2.selectbox("Select a month", months)

select_options = ["Vehicle occupancy (monthly average)", "Vehicle occupancy (morning peak hour)", "Vehicle occupancy (evening peak hour)", 
					"Passager load (monthly average)", "Passager load (morning peak hour)", "Passager load (evening peak hour)"]

col1, col2 = st.columns(2)
metric_type = col1.selectbox("Select a metric", ["Vehicle occupancy", "Passager load"])
time_period = col2.selectbox("Select a time period", ["Monthly average", "Morning peak hour", "Evening peak hour"])

metric = metric_type + time_period

datasets = importing_data(year,month)


if metric == "Vehicle occupancyMonthly average":
	most_occ, least_occ = average_occupancy(datasets[-1])
	with col1:
		st.markdown("**Top 10 track sections with higher vehicle occupancy (monthly average)**")
		st.table(most_occ)
	with col2:
		st.markdown("**Top 10 track sections with lower vehicle occupancy (monthly average)**")
		st.table(least_occ)

elif metric == "Vehicle occupancyMorning peak hour":
	most_occ, least_occ = average_occupancy(datasets[2])
	with col1:
		st.markdown("**Top 10 track sections with higher vehicle occupancy (morning peak hour)**")
		st.table(most_occ)

	with col2:
		st.markdown("**Top 10 track sections with lower vehicle occupancy (morning peak hour)**")
		st.table(least_occ)

elif metric == "Vehicle occupancyEvening peak hour":
	most_occ, least_occ = average_occupancy(datasets[12])
	with col1:
		st.markdown("**Top 10 track sections with higher vehicle occupancy (evening peak hour)**")
		st.table(most_occ)

	with col2:
		st.markdown("**Top 10 track sections with lower vehicle occupancy (evening peak hour)**")
		st.table(least_occ)

elif metric == "Passager loadMonthly average":
	most_occ, least_occ = average_passager(datasets[-1])
	with col1:
		st.markdown("**Top 10 track sections with higher passager load (monthly average)**")
		st.table(most_occ)

	with col2:
		st.markdown("**Top 10 track sections with lower passager load (monthly average)**")
		st.table(least_occ)

elif metric == "Passager loadMorning peak hour":
	most_occ, least_occ = average_passager(datasets[2])
	with col1:
		st.markdown("**Top 10 track sections with higher passager load (morning peak hour)**")
		st.table(most_occ)

	with col2:
		st.markdown("**Top 10 track sections with lower passager load (morning peak hour)**")
		st.table(least_occ)

elif metric == "Passager loadEvening peak hour":
	most_occ, least_occ = average_passager(datasets[12])
	with col1:
		st.markdown("**Top 10 track sections with higher passager load (evening peak hour)**")
		st.table(most_occ)

	with col2:
		st.markdown("**Top 10 track sections with lower passager load (evening peak hour)**")
		st.table(least_occ)
