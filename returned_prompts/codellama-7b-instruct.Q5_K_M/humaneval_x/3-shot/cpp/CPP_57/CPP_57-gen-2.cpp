    if (l.size()==1)
    return true;
    float diff=l[1]-l[0];
    for (int i=0;i<l.size()-1;i++)
    if (diff*l[i+1]<0)
    return false;
    return true;
}


