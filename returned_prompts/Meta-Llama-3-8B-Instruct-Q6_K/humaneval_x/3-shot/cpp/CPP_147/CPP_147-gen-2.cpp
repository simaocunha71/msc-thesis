    vector<int> a(n);
    int count=0;
    for (int i=1;i<=n;i++)
    {
        a[i-1]=i*i-i+1;
    }
    for (int i=0;i<n-2;i++)
    {
        for (int j=i+1;j<n-1;j++)
        {
            for (int k=j+1;k<n;k++)
            {
                if ((a[i]%3==0 && a[j]%3==0 && a[k]%3==0) || (a[i]%3!=0 && (a[j]%3+a[k]%3)%3==0))
                {
                    count++;
                }
            }
        }
    }
    return count;
}
// The idea here is to generate all possible triples and check if the sum of any of them is a multiple of 3. We can do this by checking if the sum is divisible by 3 or not. If the sum is divisible by 3 and at least one of a[i], a[j], a[k] is divisible by 3, then we count it as a valid triple. If the sum is not divisible by 3, then we also check if the sum of a[j] and a[k] is divisible by 3, and if a[i] is not divisible by 3. If this condition is also true, then we count it as a valid triple. We use three nested for loops to generate all possible triples. Inside the loops, we calculate the sum of a[i], a[j], and a[k] and check the conditions mentioned above. If the conditions are met, we increment the count. At the end of the function, we return the count of valid triples.