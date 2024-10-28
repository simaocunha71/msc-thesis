    int i=0,j=0,count=0;
    int str_len=str.length();
    int sub_len=substring.length();
    while (i<=str_len-sub_len)
    {
        for (j=0;j<sub_len;j++)
        if (str[i+j]!=substring[j])
        break;
        if (j==sub_len)
        count++;
        i++;
    }
    return count;
}


