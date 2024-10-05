    int i;
    int count=0;
    for (i=0;i<l.size()-1;i++)
    {
    if (l[i]>l[i+1])
    count+=1;
    if (l[i]<l[i+1])
    count+=2;
    }
    if (count==2)
    return false;
    else return true;
}

