    if (interval1.size()<2||interval2.size()<2)
        return "NO";
    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if (start1>end1||start2>end2)
        return "NO";
    int low=start1;
    int high=start2;
    if (low>high)
        goto A;
    low=start2;
    high=start1;
    if (low>high)
        goto A;

    int len=end1-start1;
    int len2=end2-start2;
    if (len<len2)
        return "NO";
    if (len==len2)
    {
        if (len==1)
            return "NO";
        else
            return "YES";
    }

    int i=0;
    bool flag=false;
    while (i<len)
    {
        if (start1+i==start2)
        {
            flag=true;
            break;
        }
        i++;
    }
    if (!flag)
        return "NO";
    i=0;
    flag=false;
    while (i<len)
    {
        if (start1+i==end2)
        {
            flag=true;
            break;
        }
        i++;
    }
    if (!flag)
        return "NO";
    i=0;
    flag=false;
    while (i<len2)
    {
        if (start2+i==start1)
        {
            flag=true;
            break;
        }
        i++;
    }
    if (!flag)
        return "NO";
    i=0;
    flag=false;
    while (i<len2)
    {
        if (start2+i==end1)
        {
            flag=true;
            break;
        }
        i++;
    }
    if (!flag)
        return "NO";
