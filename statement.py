gender = "female"
age = 25

if gender  == "female":
    print("ticket is free")
else:
    if age < 5:
        print("ticket is free")
    elif age <= 12:
        print("you get a child discount. half price")
    elif age >=60:  
        print("you get a senior  citizen discount.")
    else:
        print(" you pay the full price")