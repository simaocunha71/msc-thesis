    int i;
    float last=l[0];
    float next;
    for (i=1;i<l.size();i++)
    {
        next=l[i];
        if (next<last)
        return false;
        last=next;
    }
    return true;
}


