
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def largest_subset(lst):
   n = len(lst)
   if n == 1:
      return 1
   lcm = lst[0]
   for i in range(1, n):
      lcm = lcm*lst[i]//gcd(lcm, lst[i])
   return len([i for i in lst if lcm % i == 0])


