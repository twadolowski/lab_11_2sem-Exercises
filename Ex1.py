temp = input()
scale = temp[-1]
temp = float(temp[0:len(temp)-1])
if scale == "F":
    temp = (temp - 32) * 5/9
    print(temp, "C") 
elif scale == "C":
    temp = temp * 9/5 + 32
    print(temp, "F") 
