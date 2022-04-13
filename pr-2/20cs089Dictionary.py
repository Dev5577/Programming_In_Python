#StudentName :Divyaraj Sunva
#Studentid   :20CS089
#Aim         :learn Set,Dictionary,Tuple
#link(Github):

#following program for Dictionary
#Que1.Write a python script to check whether a given key is already exists in a dictionary
dect_01={'A101':'Anmol','A102':'Aaresh'}
key=input("enter key to check it is already exists in a dictionary? : ")
if key in dect_01:                   #use if else to find key
    print("key is already exist")
else:
    print("key is not present")

#Que2.Write a python script to merge two dictionaries.
dect_21={'01':'i1','02':'i2'}
dect_22={'03':'i3','04':'i4'}
dect_22.update(dect_21)              #use update() function to merge two dictionaries
print(dect_22)

#Que3.Write a python script to sum all  the item in dictionary
dect_03={'a':1,'b':2,'c':3}
values=dect_03.values()              #use sum() to function to sum all element
total=sum(values)
print(total)

#Que4.Write a python program to add key in dictionary
dect_04={'a1':10,'b1':20}            
dect_04.update({'c3':30})            #use update() to update both..
print(dect_04)

#Que5.Write a python program to concatenate following dictionaries to create a new dictionary
#all dictionary are mentioned below
dect_51={1:10,2:20}
dect_52={3:30,4:40}
dect_53={5:50,6:60}
dect_54={}
for i in [dect_51,dect_52,dect_53]:   #use for loop in update() function
    dect_54.update(i)

print(dect_54)
