import AddPerson
from main import main


while(True):
     c = input("Enter your choice \n 1. Add New Person to dataset \n 2. Train the model \n 3.Capture images to take attendance \n 4.Generate the CSV file \n 5.Exit \n\n==> YOUR CHOICE IS -> ")
     c = int(c)

     if c == 1:
         #print("New person is added")
         AddPerson.AddPerson()
     if c ==2:
        m = main()
        m.runCamera()
         