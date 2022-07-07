from datetime import datetime
str=datetime.now().strftime("%d-%m-%Y")
#print(str)
filename= "TE_"+"attendance_"+str+".csv"
#print(filename)



f= open("Att.csv","w+")
f.write("HEllo World")
f.close()

import pandas as pd

# The read_csv is reading the csv file into Dataframe

df = pd.read_csv("Att.csv")

# then to_excel method converting the .csv file to .xlsx file.

df.to_excel(filename+".xlsx", sheet_name="Testing", index=False)

# This will make a new "weather.xlsx" file in your working directory.
# This code is contributed by Vidit Varshney
