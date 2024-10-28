    int i,j,count=0;
    int str_size=str.size();
    int sub_size=substring.size();
    for (i=0;i<str_size;i++)
    {
        for (j=0;j<sub_size;j++)
        {
            if (str[i+j]!=substring[j])
            break;
            if (j==(sub_size-1))
            {
                count+=1;
            }
        }
    }
    return count;
}

