import AddPerson
from main import main


while(True):
     c = input("Enter your choice \n 1. Add New Person to dataset \n 2.Capture images to take attendance \n 3.Exit \n\n==> YOUR CHOICE IS -> ")
     c = int(c)

     if c == 1:
         #print("New person is added")
         AddPerson.AddPerson()
     if c ==2:
        m = main()
        m.runCamera()