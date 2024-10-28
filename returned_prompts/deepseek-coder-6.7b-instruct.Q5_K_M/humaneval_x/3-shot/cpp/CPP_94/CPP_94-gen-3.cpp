    int i,j,sum=0,max=0;
    for(i=0;i<lst.size();i++)
    {
        if(lst[i]>max)
        {
            max=lst[i];
        }
    }
    for(j=2;j<max;j++)
    {
        if(max%j==0)
        {
            return 0;
        }
    }
    string str = to_string(max);
    for(char& c : str) 
    {
        sum += c - '0';
    }
    return sum;
}


