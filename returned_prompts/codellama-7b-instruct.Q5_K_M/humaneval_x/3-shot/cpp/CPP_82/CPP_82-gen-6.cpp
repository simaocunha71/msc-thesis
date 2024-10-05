    int i,j,count=0;
    for (i=2;i<str.length();i++)
    for (j=2;j<i;j++)
    if (i%j==0)
    count++;
    if (count==0)
    return true;
    else
    return false;
}


