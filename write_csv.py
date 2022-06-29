from datetime import date

def Write_in_csv(): 
    f = open("Attendance.csv","a+")
    line = f.readlines()

    f1 = open("Final.csv","a+")
    today = date.today()
    DATE = today.strftime("%m/%d/%y")
    f1.writelines(f"{DATE},")
    f1.writelines(line)
    f1.close()


Write_in_csv()