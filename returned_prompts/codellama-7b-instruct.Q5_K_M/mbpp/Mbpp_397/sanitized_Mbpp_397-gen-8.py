def median_numbers(num1,num2,num3):
    num1,num2,num3 = sorted([num1,num2,num3])
    if num1 == num2 == num3:
        return num1
    elif num1 == num2:
        return (num1+num3)/2.0
    elif num1 == num3:
        return (num1+num2)/2.0
    else:
        return (num2+num3)/2.0