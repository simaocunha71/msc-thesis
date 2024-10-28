    int start1=interval1[0];
    int start2=interval2[0];
    int end1=interval1[1];
    int end2=interval2[1];
    if (start1>start2)
    {
        if (end1<start2)
        {
            return "NO";
        }
        else
        {
            if (end2<start1)
            {
                return "NO";
            }
            else
            {
                return "YES";
            }
        }
    }
    if (end1>end2)
    {
        if (start1<end2)
        {
            return "NO";
        }
        else
        {
            if (start2<end1)
            {
                return "NO";
            }
            else
            {
                return "YES";
            }
        }
    }
    if (start1==end2||end1==start2)
    {
        return "NO";
    }
    else
    {
        return "YES";
    }
}


