def power_base_sum(base,power):
    # Your code here
    sum=0
    for i in range(power):
        sum=sum+int(base)
        base=base*10
    return sum
