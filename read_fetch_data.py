import pandas
def my_main_fun():
	"""
	This is the main function
	"""
	
	#open the data(sheets) from different file formats as Panda Dataframe
	df1=pandas.read_json("supermarkets.json")
	print(df1)
	df2=pandas.read_csv("supermarkets.csv")
	df3 = pandas.read_excel("supermarkets.xlsx")
	df4=pandas.read_csv("supermarkets-commas.txt")
	df4 = pandas.read_csv("supermarkets-semi-colons.txt",sep=";")
	print(df4)
	#Now we can perform operations on it
	print(df4.Employees.max())
	print(df3.Country)
	
	#set the index as one of the column
	df3=df3.set_index("ID")
	
	#print the rows and columns in range
	print(df2.loc[1:4,"City":"Country"])
	df2.loc[:4,"City":]
	print(df2.loc[:,"Country"])
	list(df2.loc[:,"Country"])
	
	df2.iloc[1:4,3:6]
	
	
if __name__=="__main__":
	my_main_fun()