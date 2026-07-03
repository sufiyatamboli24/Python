"""Take Birthdate and calculate age and give msg Eligible for Admission if age is above 18"""
birth_year=int(input("Enter the birth year:"))
current_year=int(input("Enter the current year:"))
age=current_year-birth_year
if age>=18:
    print("eligible for addmision")
else:
   print(" Not eligible for addmision")     