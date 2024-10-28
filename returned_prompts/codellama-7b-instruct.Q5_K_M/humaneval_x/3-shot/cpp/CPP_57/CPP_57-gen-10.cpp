    int i,j;
    bool increasing=true;
    bool decreasing=true;
    for (i=0;i<l.size()-1;i++)
    {
        if (l[i]>l[i+1])
        decreasing=false;
        if (l[i]<l[i+1])
        increasing=false;
    }
    if (decreasing==true)
    return true;
    else if (increasing==true)
    return true;
    else
    return false;
}



