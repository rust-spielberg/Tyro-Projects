# SchoolName = input("School name : ")
# Name = input("Name : ")
# Class = input("Class : ")
# StartDate = input("From : ")
# EndDate = input("To : ")
# Reason = input ("Reason : ")
# Mobileno = input("Contact number : ")


# format1 = f"""
# To, 
# The Principal, 
# {SchoolName} 

# Subject: Application for Leave 

# Respected Sir/Madam, 
 
# I am {Name}, a student of {Class}. 
# I kindly request leave from {StartDate} to {EndDate} due to {Reason}. 
 
# I would be grateful if you could grant me 
# leave for the mentioned period. 
 
# Thank you. 
 
# Yours sincerely, 
# {Name} 
# {Mobileno}"""

# print(format1)






DepartmentName = input("Department Name :")
Name = input("Name : ")
StartDate = input("From : ")
EndDate = input("To : ")
Reason = input ("Reason : ")
RollNumber = input("Roll number : ")
Branch = input("Branch : ")
Year = input("Year : ")

format2 = f"""
To,
The Head of Department,
{DepartmentName}

Subject: Request for Leave

Respected Sir/Madam,

I am {Name}, a student of {Year} year, {Branch}.
I am unable to attend classes from {StartDate} to {EndDate} 
due to {Reason}.

I kindly request you to grant me leave for the mentioned period.

Thank you for your consideration.

Yours faithfully,
{Name}
{RollNumber}"""

print(format2)