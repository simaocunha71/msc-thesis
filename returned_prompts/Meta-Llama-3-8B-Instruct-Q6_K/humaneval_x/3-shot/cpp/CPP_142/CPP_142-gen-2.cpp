    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (i%3==0)
        sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0)
        sum+=pow(lst[i],3);
    }
    return sum;
}  // This code will not work correctly for large inputs because of the pow function's limited precision. 
// For large inputs, you might need to use a different method to cube the numbers. 
// For example, you could use the fact that a^3 = (a^(1/3))^3, which would allow you to compute the cube without losing precision.  // This could be implemented as follows:
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (i%3==0)
        sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0)
        sum+=pow(pow(lst[i],1.0/3.0),3);
    }
    return sum;
}  // This code will still not work correctly for very large inputs, because the pow function's result may be too large to fit in an int.  // For very large inputs, you would need to use a different method to compute the sum. 
// For example, you could use a long long to store the sum, and then convert it to an int at the end.  // This could be implemented as follows:
int sum_squares(vector<int> lst){
    long long sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (i%3==0)
        sum+=(long long)lst[i]*(long long)lst[i];
        else if (i%4==0 && i%3!=0)
        sum+=(long long)pow(pow(lst[i],1.0/3.0),3);
    }
    return (int)sum;
}  // This code will still not work correctly for very, very large inputs, because the pow function's result may be too large to fit in a long long.  // For very, very large inputs, you would need to use a different method to compute the sum. 
// For example, you could use a library that provides arbitrary-precision arithmetic, such as the GNU Multiple