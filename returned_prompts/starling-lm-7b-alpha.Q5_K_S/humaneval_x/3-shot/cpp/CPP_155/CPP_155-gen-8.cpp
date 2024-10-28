    vector<int> res;
    int i,count=0;
    for (i=0;i<abs(num);i++)
    {
        if (num%2==0) count+=1;
        num/=10;
    }
    res.push_back(count);
    res.push_back(abs(num)-count);
    return res;
}


