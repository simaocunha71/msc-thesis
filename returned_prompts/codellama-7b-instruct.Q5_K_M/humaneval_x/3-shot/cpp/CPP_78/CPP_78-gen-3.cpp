    int i;
    int count=0;
    int j;
    for (i=0;i<num.length();i++)
    {
        j=num[i]-'A';
        if (j%2==1)
        count+=1;
    }
    return count;
}



