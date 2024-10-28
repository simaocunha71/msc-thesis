    int i,counter=0,length=substring.length();
    for (i=0;i<str.length();i++)
    {
        int j;
        for (j=0;j<length;j++)
        {
            if (str[i+j]!=substring[j])
            break;
        }
        if (j==length)
        counter++;
    }
    return counter;
}


