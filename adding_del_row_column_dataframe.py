import pandas

def new_fun():
	df=pandas.read_csv("supermarkets.csv")
	df.set_index("ID")
	print(df)
	print("\n")
	#To delete the column pass column name and 1 as second argument in drop command
	#This is not inplace function
	df1 = df.drop("City",1)
	print(df1)
	print("\n")
	
	#To delete the row pass row name and 0 as second argument in drop command
	#This is not inplace function
	df2 = df.drop(3,0)
	print(df2)
	print("\n")
	#to delete multiple rows at once
	df2 = df.drop(df.index[1:4],0)
	print(df2)
	print("\n")
	
	
	#Adding a new columns 
	df["New_column"] = ["a","b","c","d","e","f"]
	print(df)
	print("\n")
	
	#updating the values in column
	df["New_column"] = df.shape[0]*["new_value"]
	print(df)
	print("\n")
	
	#updating only single values
	df.loc[3,"New_column"]="Brand_new"
	print(df)
	print("\n")
	
	
	#Adding new row: For this flip the rows and columns and add new column
	df_temp=df.T
	#print(df_temp)
	#print("\n")
	
	df_temp[6]=[7,"new st","new city","new state","new country","new name",12,"new_value"]
	df = df_temp.T
	print(df)
	print("\n")
	
	
if __name__=="__main__":
	new_fun()