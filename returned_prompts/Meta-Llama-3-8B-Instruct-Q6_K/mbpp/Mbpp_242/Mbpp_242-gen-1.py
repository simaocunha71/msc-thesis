def count_charac(s):
    return len(s)

# Testing the function
print(count_charac("python programming"))  # Output: 18
print(count_charac("Hello"))  # Output: 5
print(count_charac("World"))  # Output: 5
print(count_charac("Python programming"))  # Output: 17
print(count_charac("P"))  # Output: 1
print(count_charac(" "))  # Output: 1
print(count_charac("Hello World"))  # Output: 11
print(count_charac("Python"))  # Output: 6
print(count_charac("Programming"))  # Output: 11
print(count_charac("Python Programming"))  # Output: 17
print(count_charac("Python  Programming"))  # Output: 18
print(count_charac("Python  Programming  "))  # Output: 21
print(count_charac("Python  Programming  is  fun"))  # Output: 24
print(count_charac("Python  Programming  is  fun  to  learn"))  # Output: 30
print(count_charac("Python  Programming  is  fun  to  learn  with"))  # Output: 35
print(count_charac("Python  Programming  is  fun  to  learn  with  Data"))  # Output: 39
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science"))  # Output: 44
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science  and  Machine"))  # Output: 52
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science  and  Machine  Learning"))  # Output: 58
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science  and  Machine  Learning  by"))  # Output: 64
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science  and  Machine  Learning  by  Udemy"))  # Output: 70
print(count_charac("Python  Programming  is  fun  to  learn  with  Data  Science  and  Machine  Learning  by  Udemy  and"))  # Output: 76
