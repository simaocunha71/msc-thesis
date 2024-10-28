
def anti_shuffle(s):
    return " ".join(sorted(word) for word in s.split())




# Made By Mostafa_Khaled
```
    
    
        

        




        




        

        


        



```



```*************************************************************/
import sys
import math
from collections import defaultdict

#sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def rstr():
    s = input()
    return list(s[:len(s) - 1])

def get_num_2_5(n):
    cnt_2 = 0
    cnt_5 = 0
    while n >= 2:
        cnt_2 += n // 2
        n //= 2
    while n >= 5:
        cnt_5 += n // 5
        n //= 5
    return (cnt_2, cnt_5)

def get_num_2_5_3(n):
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    while n >= 2:
        cnt_2 += n // 2
        n //= 2
    while n >= 3:
        cnt_3 += n // 3
        n //= 3
    while n >= 5:
        cnt_5 += n // 5
        n //= 5
    return (cnt_2, cnt_3, cnt_5)





def solve():
    pass




if __name__ == "__main__":
    solve()


```*********************************************************/
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

```

``