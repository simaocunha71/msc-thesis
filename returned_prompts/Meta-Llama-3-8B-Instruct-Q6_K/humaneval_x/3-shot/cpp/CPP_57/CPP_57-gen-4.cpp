    bool increasing=true;
    bool decreasing=true;
    for (int i=0;i<l.size()-1;i++)
    {
        if (l[i+1]>l[i])
        {
            decreasing=false;
        }
        if (l[i+1]<l[i])
        {
            increasing=false;
        }
    }
    return increasing || decreasing;
}
