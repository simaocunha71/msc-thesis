
def hex_key(num):
    hex_list = [str(i) for i in range(10)]
    hex_list += ["A", "B", "C", "D", "E", "F"]

    primes = [2, 3, 5, 7, 11, 13, 17]

    primes_dict = {str(i): 0 for i in hex_list}

    for i in range(len(num)):
        if num[i] in hex_list:
            primes_dict[num[i]] += primes[int(num[i]) - 10]
        else:
            primes_dict[num[i]] += int(num[i])

    return sum(primes_dict[i] for i in hex_list if primes_dict[i] > 0)











```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
```