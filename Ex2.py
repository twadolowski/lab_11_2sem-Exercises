print("Introduce day:")
day = int(input())
print("Introduce month:")
month = int(input())
season = ""
isDateCorrect = True

if day>31 or month>12:
    isDateCorrect = False

elif (month%2 == 0 and month<7) or (month%2==1 and month>8):    
    if day>29 and month==2:
        isDateCorrect = False    
    elif day>30:
        isDateCorrect = False

if isDateCorrect:
    if month<3:
        season="Winter"
    elif month==3 and day>20:
        season="Spring"
    elif month<6 or (month==6 and day<21): 
        season="Spring"
    elif month<9 or (month==9 and day<21):
        season="Summer"
    elif month<12 or (month==12 and day<21):
        season="Fall"
    else: 
        season="Winter"

    print(season)

else:
    print("Incorrect Date")
