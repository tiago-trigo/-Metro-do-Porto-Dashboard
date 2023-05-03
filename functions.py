import pandas as pd
import numpy as np

def importing_data(year,month):
	if year == "2018":
		df6 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 6h-7h.csv")
		df7 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 7h-8h.csv")
		df8 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 8h-9h.csv")
		df9 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 9h-10h.csv")
		df10 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 10h-11h.csv")
		df11 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 11h-12h.csv")
		df12 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 12h-13h.csv")
		df13 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 13h-14h.csv")
		df14 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 14h-15h.csv")
		df15 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 15h-16h.csv")
		df16 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 16h-17h.csv")
		df17 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 17h-18h.csv")
		df18 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 18h-19h.csv")
		df19 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 19h-20h.csv")
		df20 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 20h-21h.csv")
		df21 = pd.read_csv(f"Data/Cleaned/{year}/{month}/Média 21h-22h.csv")
		df22 = pd.read_csv(f"Data/Cleaned/{year}/{month}//Média 22h-23h.csv")
		df23 = pd.read_csv(f"Data/Cleaned//{year}/{month}/Média 23h-0h.csv")
		df_average = pd.read_csv(f"Data/Cleaned//{year}/{month}/Média Mensal.csv")

	elif year == "2019":
		df6 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 6h-7h.csv")
		df7 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 7h-8h.csv")
		df8 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 8h-9h.csv")
		df9 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 9h-10h.csv")
		df10 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 10h-11h.csv")
		df11 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 11h-12h.csv")
		df12 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 12h-13h.csv")
		df13 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 13h-14h.csv")
		df14 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 14h-15h.csv")
		df15 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 15h-16h.csv")
		df16 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 16h-17h.csv")
		df17 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 17h-18h.csv")
		df18 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 18h-19h.csv")
		df19 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 19h-20h.csv")
		df20 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 20h-21h.csv")
		df21 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 21h-22h.csv")
		df22 = pd.read_csv(f"Data/Cleaned/{year}/{month}{year}/Média 22h-23h.csv")
		df23 = pd.read_csv(f"Data/Cleaned//{year}/{month}{year}/Média 23h-0h.csv")
		df_average = pd.read_csv(f"Data/Cleaned//{year}/{month}{year}/Média Mensal.csv")

	return df6, df7, df8 ,df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df_average 

def average_occupancy(df):
	df_OccAB = df[["A", "B", "OccupancyAtoB"]]
	df_OccBA = df[["A", "B", "OccupancyBtoA"]]
	col_list = list(df_OccBA)
	col_list[0], col_list[1] = col_list[1], col_list[0]
	df_OccBA.columns = col_list
	df_OccAB = df_OccAB.rename(columns = {"A": "Station A", "B": "Station B", "OccupancyAtoB" : "Vehicle occupancy (%)"})
	df_OccBA = df_OccBA.rename(columns = {"A": "Station A", "B": "Station B", "OccupancyBtoA" : "Vehicle occupancy (%)"})
	df_most = pd.concat([df_OccAB, df_OccBA]).sort_values(by = ["Vehicle occupancy (%)"], ascending = False).head(10).reset_index(drop = True)
	df_most.index = np.arange(1, len(df_most) + 1)
	df_most["Vehicle occupancy (%)"] = np.round(df_most["Vehicle occupancy (%)"] * 100,2)
	df_least = pd.concat([df_OccAB, df_OccBA]).sort_values(by = ["Vehicle occupancy (%)"]).head(10).reset_index(drop = True)
	df_least.index = np.arange(1, len(df_least) + 1)
	df_least["Vehicle occupancy (%)"] = np.round(df_least["Vehicle occupancy (%)"] * 100,2)

	return df_most, df_least


def average_passager(df):
	df_PassAB = df[["A", "B", "PassagersAtoB"]]
	df_PassBA = df[["A", "B", "PassagersBtoA"]]
	col_list = list(df_PassBA)
	col_list[0], col_list[1] = col_list[1], col_list[0]
	df_PassBA.columns = col_list
	df_PassAB = df_PassAB.rename(columns = {"A": "Station A", "B": "Station B", "PassagersAtoB" : "Number of passagers"})
	df_PassBA = df_PassBA.rename(columns = {"A": "Station A", "B": "Station B", "PassagersBtoA" : "Number of passagers"})
	df_most = pd.concat([df_PassAB, df_PassBA]).sort_values(by = ["Number of passagers"], ascending = False).head(10).reset_index(drop = True)
	df_most.index = np.arange(1, len(df_most) + 1)
	df_most["Number of passagers"] = np.round(df_most["Number of passagers"])
	df_least = pd.concat([df_PassAB, df_PassBA]).sort_values(by = ["Number of passagers"]).head(10).reset_index(drop = True)
	df_least.index = np.arange(1, len(df_least) + 1)
	df_least["Number of passagers"] = np.round(df_least["Number of passagers"])
	
	return df_most, df_least


def list_maker(A, B, dataset_list):
	occupancy = []
	tramtrains = []
	eurotrams = []
	AtoB = []
	BtoA = []
	PassAtoB = []
	PassBtoA = []

	for dataset in dataset_list[:-1]:
	    
	    data = dataset[(dataset["A"] == A) & (dataset["B"] == B)]
	    
	    if data.empty:
	        data = dataset[(dataset["A"] == B) & (dataset["B"] == A)]
	        

	    occupancy.append(float(data["OccupancyTotal"]))
	    tramtrains.append(float(data["TraintramTotal"]))
	    eurotrams.append(float(data["EurotramTotal"]))
	    AtoB.append(float(data["OccupancyAtoB"]))
	    BtoA.append(float(data["OccupancyBtoA"]))

	return occupancy, tramtrains, eurotrams, AtoB, BtoA, PassAtoB, PassBtoA, data["A"].iloc[0], data["B"].iloc[0]