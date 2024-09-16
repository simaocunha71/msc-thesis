def armstrong_number(num):
    temp=num
    count=0
    while temp>0:
        count+=1
        temp//=10
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**count
        temp//=10
    if sum==num:
        return True
    else:
        return False



