    int sum=0;
    for(int i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    if(sum>w)
    {
        return false;
    }
    int start = 0;
    int end = q.size() - 1;
    while (start < end)
    {
        if (q[start] != q[end])
        {
            return false;
        }
        start++;
        end--;
    }
    return true;
}



