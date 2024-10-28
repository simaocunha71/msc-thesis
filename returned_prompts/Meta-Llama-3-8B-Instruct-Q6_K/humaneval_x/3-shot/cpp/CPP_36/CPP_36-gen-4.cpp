    int count=0;
    for (int i=11; i<n; i++)
    {
        if (i%11==0 || i%13==0)
        {
            while (i>0)
            {
                if (i%10==7)
                {
                    count++;
                    break;
                }
                i /= 10;
            }
        }
    }
    for (int i=13; i<n; i++)
    {
        if (i%11==0 || i%13==0)
        {
            while (i>0)
            {
                if (i%10==7)
                {
                    count++;
                    break;
                }
                i /= 10;
            }
        }
    }
    return count;
}  



