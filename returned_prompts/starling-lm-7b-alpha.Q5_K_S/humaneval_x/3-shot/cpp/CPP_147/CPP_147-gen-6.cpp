    vector<int> numbers;
    int i;
    int result=0;
    for (i=0;i<n;i++)
    {
        numbers.push_back(i*i-i+1);
    }
    for (i=0;i<n;i++)
    for (int j=i+1;j<n;j++)
    for (int k=j+1;k<n;k++)
    {
        if ((numbers[i]+numbers[j]+numbers[k])%3==0)
        result+=1;
    }
    return result;
}


