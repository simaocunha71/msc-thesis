    int max=0;
    int count=0;
    for (int i=1;i<lst.size();i++)
    {
        if (lst[i]>max)
        {
            max=lst[i];
            count=0;
            for (int j=0;j<lst.size();j++)
            {
                if (lst[j]==max)
                    count++;
            }
            if (count>=max)
                return max;
        }
    }
    return -1;
} 