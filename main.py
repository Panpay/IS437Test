year = input("Enter year: \n")
# must be between 1900 and 2020
try:
    yeari = int(year)
except:
    pass
if yeari is not None:
    
    if yeari < 1900:
        print("Year must be greater than 1900.")
    elif year > 2020:
        print("Year must be less than 2020.")
    else:
        print("Year is valid")
else:
    print("Year "+year+" is invalid.")