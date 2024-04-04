import pathlib
import os

file8= pathlib.Path("carDatabase.txt")
R= "{} Model {} No {} Manufactured in {} \n"

class Cars:
  def __init__(self, a, b1, b2, c):
    self.manu= a
    self.modalNa= b1
    self.modalNo= b2
    self.YOM= c
    
  def __repr__(self):
    self.r= R.format(self.manu, self.modalNa, self.modalNo, self.YOM)
    return self.r

print("1. Do you want to add a new entry to the database: '+' \n\t OR \n\t 2. Do you want to read the existing specifications: '=' \n\t OR \n\t 3. Do you wish to delete an existing entry: '-'")
o= input()
if o == "+":
  z= input("Enter the name of the car manufaturer: ")
  y1= input("Enter the modal name: ")
  y2= input("Enter the modal number: ")
  x= int(input("Enter the year of manufacture: "))
  car= Cars(z,y1,y2,x)
  print(car)
  
  try:
    if file8.exists():
      with open("carDatabase.txt","a") as file1:
        file1.write(R.format(z,y1,y2,x))
    else:
        print("0")
  except Exception as eh:
    eh= "File does not exist"
    print("There was an error-->",eh,"and that is corrected now you can continue")
    with open("carDatabase.txt","w") as file9:
      file1.write(R.format(z,y1,y2,x))
  finally:
    print("\n\t Done")

elif o== "=":
  try:
    if file8.exists():
      file2= open("carDatabase.txt")
      print("The cars in the database are : \n",file2.read())
      print("\n\t Done")
    else:
      print("0")
  except Exception as eh:
    eh= "File does not exist"
    print("There was an error-->",eh,"and that is corrected now you can continue")
    with open("carDtabase.txt","w") as file7:
      file7.write("")
  finally:
    print("\n\t Done")
    
elif o== "-":
  try:
    if file8.exists():
      file3= open("carDatabase.txt")
      p= file3.read()
      print(p)
    else:
      print("0")
  except Exception as eh:
    eh= "File does not exist"
    print("There was an error-->",eh,"and that is corrected now you can continue")
    with open("carDatabase.txt","w") as file7:
      file7.write("")
  finally:
      print("\n\t Done")
