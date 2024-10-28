    int sum=0;
    int i,j;
    for(i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    if(sum>w)
    {
        return false;
    }
    i=0;
    j=q.size()-1;
    while(i<j)
    {
        if(q[i]==q[j])
        {
            i++;
            j--;
        }
        else
        {
            return false;
        }
    }
    return true;
}


