def armstrong_number(n):
    if n>9:
        s=0
        temp=n
        while temp>0:
            rem = temp%10
            s+=rem**4
            temp//=10
        if s==n:
            return True
        else:
            return False
    else:
        return False