    long long sum=0;
    for (float num:lst)
    if (num>0 && modf(num,&num)==0)
    sum+=num*num;
    return sum;
} 
// modf returns the fractional part of the number in the second argument
// It returns the integer part in the first argument. For example, modf(3.5,&num) would put 3 in num and 0.5 in return value.
// Since we are only interested in integer part, we don't need the return value. We just use it to get the integer part.  modf() returns the fractional part. If the number is an integer, then fractional part is 0. So if modf() returns 0, the number is an integer.  



