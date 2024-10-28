    int i;
    float max=0;
    for (i=0;i<l.size();i++)
    {
        if (max<l[i])
        max=l[i];
    }
    return max;
}

