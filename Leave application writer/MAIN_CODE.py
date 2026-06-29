# print("Leave Application Generator")
# print("1. School Student")
# print("2. College Student")
# print("3. Working Individual")

# choice = input("Enter your choice (1/2/3): ")

# if choice == "1":
#     SchoolName = input("School name : ")
#     Name = input("Name : ")
#     Class = input("Class : ")
#     StartDate = input("From : ")
#     EndDate = input("To : ")
#     Reason = input("Reason : ")
#     Mobileno = input("Contact number : ")


#     format1 = f"""
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

#     print(format1)

# elif choice == "2":
#     DepartmentName = input("Department Name :")
#     Name = input("Name : ")
#     StartDate = input("From : ")
#     EndDate = input("To : ")
#     Reason = input("Reason : ")
#     RollNumber = input("Roll number : ")
#     Branch = input("Branch : ")
#     Year = input("Year : ")

#     format2 = f"""
# To,
# The Head of Department,
# {DepartmentName}

# Subject: Request for Leave

# Respected Sir/Madam,

# I am {Name}, a student of {Year} year, {Branch}.
# I am unable to attend classes from {StartDate} to {EndDate} 
# due to {Reason}.

# I kindly request you to grant me leave for the mentioned period.

# Thank you for your consideration.

# Yours faithfully,
# {Name}
# {RollNumber}"""

#     print(format2)

# elif choice == "3":
#     BossName = input ("BossName : ")
#     CompanyName = input("CompanyName : ")
#     EmployeeName = input("Name : ")
#     StartDate = input("From : ")
#     EndDate = input("To : ")
#     Reason = input("Reason : ")   
#     EmployeeID = input("EmployeeID : ") 


#     format3 = f"""
# To,
# {BossName}
# {CompanyName}

# Subject: Leave Request

# Dear Sir/Madam,

# I would like to request leave from {StartDate} to {EndDate}
# due to {Reason}.

# I will ensure that my pending work is completed or properly handed
# over before my leave period.

# I kindly request you to approve my leave.

# Thank you for your understanding.

# Sincerely,
# {EmployeeName}
# {EmployeeID}
# """
#     print(format3)