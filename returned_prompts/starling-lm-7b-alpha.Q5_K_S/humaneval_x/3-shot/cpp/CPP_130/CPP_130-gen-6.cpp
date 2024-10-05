    vector<int> numbers;
    int i,j;
    if (n==0)
    return numbers;
    numbers.push_back(3);
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        numbers.push_back(1+i/2);
        else
        {
            j=i-1;
            while (j<i-2)
            {
                if (j%2==0)
                numbers.push_back(1+j/2);
                else
                {
                    j+=3;
                    j%=n+1;
                }
            }
            numbers.push_back(numbers[j]+numbers[j+1]+numbers[j+2]);
        }
    }
    return numbers;
}


