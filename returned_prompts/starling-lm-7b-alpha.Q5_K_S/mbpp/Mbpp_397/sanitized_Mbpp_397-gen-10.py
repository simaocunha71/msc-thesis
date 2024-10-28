def median_numbers(x,y,z):
    # your code here
    a=[x,y,z]
    a.sort()
    if len(a)%2==0:
        return (a[len(a)//2]+a[len(a)//2-1])/2
    else:
        return a[len(a)//2]