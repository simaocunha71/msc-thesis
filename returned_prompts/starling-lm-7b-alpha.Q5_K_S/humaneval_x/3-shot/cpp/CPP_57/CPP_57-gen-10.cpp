    int i;
    float prev=-1000;
    for (i=0;i<l.size();i++)
    {
        if (prev<l[i])
        {
            prev=l[i];
        }
        else
        {
            return false;
        }
    }
    return true;
}


