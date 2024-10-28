    vector<int> tmp;
    tmp=nums;
    int i,j;
    for (i=0;i<tmp.size();i++)
    {
        for (j=i+1;j<tmp.size();j++)
        {
            if ((sum_of_digits(tmp[i])+tmp[i])>(sum_of_digits(tmp[j])+tmp[j]))
            {
                int temp=tmp[i];
                tmp[i]=tmp[j];
                tmp[j]=temp;
            }
        }
    }
    return tmp;
}

