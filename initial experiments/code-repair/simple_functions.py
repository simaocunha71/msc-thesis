def find_common(list1, list2):
    """ Returns the common elements in list1 and list2 """
    common = []
    for elem in list1:
        if elem in list2 and elem not in common:
            common.append(elem)
    return common

def calculate_prime_numbers(n):
    prime_numbers = []
    i = 2
    while len(prime_numbers) <= n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
        i += 1
    return prime_numbers

def calculate_prime_numbers_up_to(n):
  prime_numbers = []
  
  for num in range(2, n+1):
    for i in range(2, num):
      if (num % i == 0):
        break
    else:
      prime_numbers.append(num)
  
  return prime_numbers

def calculate_prime_numbers_up_to2(num):
  prime_numbers = []
  for i in range(2, num+1):
    is_prime = True
    for j in range(2, i):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      prime_numbers.append(i)
  return prime_numbers

def calculate_prime_numbers_up_to3(num):
    prime_numbers = []
    for number in range(2, num+1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            prime_numbers.append(number)
    return prime_numbers

def calculate_prime_numbers_up_to4(n):
  prime_numbers = []
  for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
      if num % i == 0:
        prime = False
    if prime:
      prime_numbers.append(num)
  return prime_numbers
