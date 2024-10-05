    int i,j,k,l;
    int change=0;
    int size=arr.size();
    int *freq=new int[size];
    int *freq2=new int[size];
    int *freq_min=new int[size];
    int min_change=size;

    //frequency of each element
    for (i=0;i<size;i++)
    {
        freq[arr[i]]+=1;
    }

    //frequency of each element in other order
    for (i=0;i<size;i++)
    {
        freq2[i]=0;
        for (j=0;j<size;j++)
        {
            if (arr[j]==i)
            freq2[i]+=1;
        }
    }

    //minimum frequency of any element
    for (i=0;i<size;i++)
    {
        freq_min[i]=freq[i];
        for (j=0;j<size;j++)
        {
            if (freq2[j]<freq_min[i])
            freq_min[i]=freq2[j];
        }
    }

    //number of changes needed
    for (i=0;i<size;i++)
    {
        change+=abs(freq[i]-freq_min[i]);
    }

    delete[] freq;
    delete[] freq2;
    delete[] freq_min;
    return change;
}


