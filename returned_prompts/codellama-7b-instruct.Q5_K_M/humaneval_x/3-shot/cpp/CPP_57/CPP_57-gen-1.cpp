    float diff=l[1]-l[0];
    for (int i=1;i<l.size();i++)
    {
        if ((l[i]-l[i-1])*diff<0)
        return false;
    }
    return true;
}


