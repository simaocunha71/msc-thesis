"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def perrin_number(n):
    result = ""
    number = str(n)
    for character in number:
        if (character>5 and character<10) or (character==12 and character!=10):
            result += str(character + 1)
            print(result)
            
def cal_sum(n):
    perrin = []
    
    for number in range(1, n+1):
        if not any(1<int(number)<=9 and int(number)>4 or int(number)=12 for i in perrin):
            perrin.append(int(number))
    return sum(range(1,n+1))
