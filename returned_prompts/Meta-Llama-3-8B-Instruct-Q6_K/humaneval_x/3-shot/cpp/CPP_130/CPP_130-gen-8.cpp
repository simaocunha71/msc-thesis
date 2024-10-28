    vector<int> result;
    result.push_back(1);
    result.push_back(3);
    for(int i=2;i<n+1;i++)
    {
        if(i%2==0)
        {
            result.push_back(1+i/2);
        }
        else
        {
            int a=result[i-1],b=result[i-2],c=result[i-3];
            result.push_back(a+b+c);
        }
    }
    return result;
}  



