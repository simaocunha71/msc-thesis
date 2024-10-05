    if(n>m) return "-1";
    float sum=0;
    for(int i=n;i<=m;i++)
    {
        sum+=i;
    }
    float average=sum/(m-n+1);
    int avg=round(average);
    if(avg<0) return "-1";
    string res="";
    while(avg>0)
    {
        if(avg&1) res='1'+res;
        else res='0'+res;
        avg>>=1;
    }
    return res;
}  // 1. Check if n is greater than m, return "-1". 
   // 2. Calculate the sum of integers from n to m.
   // 3. Calculate the average by dividing the sum by (m-n+1).
   // 4. Round the average to the nearest integer.
   // 5. Convert the integer to binary and return it as a string.  //6. If the result is negative, return "-1".  //7. Return the result.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  // 