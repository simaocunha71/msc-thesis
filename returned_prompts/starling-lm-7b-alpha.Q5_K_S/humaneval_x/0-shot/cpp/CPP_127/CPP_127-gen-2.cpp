    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if(start1>end2||start2>end1)
    {
        return "NO";
    }
    else if(start1>=start2&&start1<=end2)
    {
        if(start2<=end1&&start2>=start1)
        {
            int length=end1-start2+1;
            for(int i=2;i<length;i++)
            {
                if(length%i==0)
                {
                    return "NO";
                }
            }
            return "YES";
        }
        else if(end2<=end1&&end2>=start1)
        {
            int length=end2-start1+1;
            for(int i=2;i<length;i++)
            {
                if(length%i==0)
                {
                    return "NO";
                }
            }
            return "YES";
        }
    }
    else if(start2>=start1&&start2<=end1)
    {
        if(start1<=end2&&start1>=start2)
        {
            int length=end2-start1+1;
            for(int i=2;i<length;i++)
            {
                if(length%i==0)
                {
                    return "NO";
                }
            }
            return "YES";
        }
        else if(end1<=end2&&end1>=start2)
        {
            int length=end1-start2+1;
            for(int i=2;i<length;i++)
            {
                if(length%i==0)
                {
                    return "NO";
                }
            }
            return "YES";
        }
    }
    else if(end2>=start1&&end2<=end1)
    {
        int length=end2-start1+1;
        for(