SchoolName = input("School name : ")
Name = input("Name : ")
Class = input("Class : ")
StartDate = input("From : ")
EndDate = input("To : ")
Reason = input ("Reason : ")
Mobileno = input("Contact number : ")


format1 = f"""
To, 
The Principal, 
{SchoolName} 

Subject: Application for Leave 

Respected Sir/Madam, 
 
I am {Name}, a student of {Class}. 
I kindly request leave from {StartDate} to {EndDate} due to {Reason}. 
 
I would be grateful if you could grant me 
leave for the mentioned period. 
 
Thank you. 
 
Yours sincerely, 
{Name} 
{Mobileno}"""

print(format1)