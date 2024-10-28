    vector<int> sorted;
    vector<int> ones;
    for (int i=0;i<arr.size();i++)
    {
        int num=arr[i];
        int binary=num;
        int count=0;
        while (binary>0)
        {
            if (binary%2==1)
            count+=1;
            binary/=2;
        }
        ones.push_back(count);
    }
    vector<int> dec;
    for (int i=0;i<arr.size();i++)
    {
        int num=arr[i];
        int binary=num;
        int count=0;
        while (binary>0)
        {
            if (binary%2==1)
            count+=1;
            binary/=2;
        }
        dec.push_back(count);
    }
    for (int i=0;i<arr.size();i++)
    {
        int num=arr[i];
        int binary=num;
        int count=0;
        while (binary>0)
        {
            if (binary%2==1)
            count+=1;
            binary/=2;
        }
    }
    sort(dec.begin(),dec.end());
    for (int i=0;i<arr.size();i++)
    {
        int num=arr[i];
        int binary=num;
        int count=0;
        while (binary>0)
        {
            if (binary%2==1)
            count+=1;
            binary/=2;
        }
        if (ones[i]==dec[i])
        {
            sorted.push_back(arr[i]);
        }
        else if (ones[i]<dec[i])
        {
            int j;
            for (j=0;j<arr.size();j++)
            {
                if (ones[j]==ones[i]+1 && dec[j]==dec[i]-1)
                {
                    sorted.push_back(arr[j]);
                    break;
                }
            }
       