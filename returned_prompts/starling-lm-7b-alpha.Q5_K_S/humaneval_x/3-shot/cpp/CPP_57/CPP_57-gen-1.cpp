    int i;
    if (l.size()==0) return true;
    for (i=1;i<l.size();i++)
    if ((l[i]-l[i-1])*(l[i]-l[i-1])<0) return false;

    return true;
}


