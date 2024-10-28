
def amicable_numbers_sum(n):
  amicable_numbers = [sum(d/d1 for d in range(1,int(math.sqrt(d))+1) if d%(d1)==0) for d in range(1,n+1) if sum(d/d1 for d in range(1,int(math.sqrt(d))+1) if d%(d1)==0)<4]
  return sum(amicable_numbers)


