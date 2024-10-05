    int i,count=0;
    int length_str=str.length();
    int length_substr=substring.length();

    for (i=0;i<length_str;i++)
    {
        int j;
        for (j=0;j<length_substr;j++)
        {
            if (str[i+j]!=substring[j])
            break;
        }
        if (j==length_substr)
        {
        count+=1;
        }
    }
    return count;
}



