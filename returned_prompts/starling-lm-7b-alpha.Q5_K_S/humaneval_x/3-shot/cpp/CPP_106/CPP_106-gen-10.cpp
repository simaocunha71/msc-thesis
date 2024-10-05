    vector<int> all;
    int i,j;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        {
            j=i;
            while (j>1)
            {
                j-=1;
                if (j==1)
                all.push_back(j);
                else
                all.push_back(j*i);
            }
        }
        else
        {
            j=i;
            while (j>0)
            {
                j-=1;
                if (j==0)
                all.push_back(j);
                else
                all.push_back(j);
            }
        }
    }
    return all;
}


