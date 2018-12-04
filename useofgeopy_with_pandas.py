import pandas
from geopy.geocoders import ArcGIS
def new_fun(st):
	nom=ArcGIS()
	#print(type(nom))
	#print("\n")
	#print(nom.geocode("38 Elm st, New York,USA"))
	try:
		xst = nom.geocode(st)
	except:
		return None
	else:
		return xst
def call_main_fun():
	df = pandas.read_csv("supermarkets.csv")
	print(df)
	print("\n")

	
	print("\n")
	df["Cordinates"]=df["Address"]+", "+df["City"]+ ", "+df["State"]+ ", "+df["Country"]
	print(df)
	print("\n")
	#the way to apply function on column  of dataframe
	
	df["Cordinates"]=df["Cordinates"].apply(new_fun)
	print(df)
	print("\n")
	df["Longitude"]=df["Cordinates"].apply(lambda x:x.longitude if x != None else None)
	df["Latitude"]=df["Cordinates"].apply(lambda x:x.latitude if x!=None else None)
	
	print(df)
	print("\n")
if __name__=="__main__":
	call_main_fun()
