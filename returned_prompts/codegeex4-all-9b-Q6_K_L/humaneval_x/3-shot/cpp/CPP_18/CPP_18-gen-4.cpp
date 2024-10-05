    int i;
    int count=0;
    int str_length=str.length();
    int sub_length=substring.length();

    for (i=0;i<str_length;i++)
    {
        if (str[i]==substring[0])
        {
            int j;
            for (j=0;j<sub_length;j++)
            if (str[i+j]!=substring[j])
            break;
            if (j==sub_length)
            count+=1;
        }
    }
    return count;
}