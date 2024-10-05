    int i;
    for(i=n/2;i>1;i--)
    {
        if(n%i==0)
        {
            while(n%i==0)
            {
                n=n/i;
            }
        }
    }
    return n;
} 
// This is a very inefficient solution. It can be improved by using a sieve to find all prime numbers up to sqrt(n) and then checking if any of these numbers divide n. This would reduce the time complexity from O(n) to O(sqrt(n)).
// Also, the function will return the last prime factor, not the largest. This can be fixed by comparing the current prime factor with the previous one and updating the result if necessary. 

