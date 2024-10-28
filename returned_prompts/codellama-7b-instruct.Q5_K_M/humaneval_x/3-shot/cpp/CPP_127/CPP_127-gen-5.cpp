    int start1=interval1[0],end1=interval1[1];
    int start2=interval2[0],end2=interval2[1];
    if (start1>end1)
    {
        int temp=start1;
        start1=end1;
        end1=temp;
    }
    if (start2>end2)
    {
        int temp=start2;
        start2=end2;
        end2=temp;
    }
    int max_start=max(start1,start2);
    int min_end=min(end1,end2);
    if (max_start>min_end)
    return "NO";
    else
    {
        int len=min_end-max_start+1;
        if (len==1)
        return "NO";
        else
        {
            for (int i=2;i<len;i++)
            if (len%i==0)
            return "NO";
            else
            return "YES";
        }
    }
}


