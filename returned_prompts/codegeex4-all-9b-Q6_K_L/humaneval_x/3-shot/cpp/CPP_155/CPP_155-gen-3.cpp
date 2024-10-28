    int i;
    int even=0,odd=0;
    for (i=0;num>0;i++)
    {
        if (num%2==0)
        even+=1;
        else
        odd+=1;
        num=num/10;
    }
    vector<int> evenodd;
    evenodd.push_back(even);
    evenodd.push_back(odd);
    return evenodd;
}

