    int i;
    float prev=0;
    for (i=0;i<l.size();i++)
    {
        if (i==0)
        {
            prev=l[i];
            continue;
        }
        if (l[i]>prev&&l[i+1]<prev)
        return false;
        if (l[i]<prev&&l[i+1]>prev)
        return false;
        prev=l[i];
    }
    return true;
}


