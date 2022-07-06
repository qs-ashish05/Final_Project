from datetime import date
import pandas as pd

def Write_in_csv(namelist): 
    namelist = namelist

    today = date.today()
    DATE = today.strftime("%m/%d/%y")

    column = {DATE : namelist}

    df = pd.DataFrame(column,columns=[DATE])

    df.to_csv(f"Attendane_of_Today.csv")
    print('File is generated')