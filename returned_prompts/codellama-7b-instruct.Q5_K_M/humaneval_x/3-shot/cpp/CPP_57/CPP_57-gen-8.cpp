    if (l.size()==1)
    return true;
    else{
        if (l[1]>l[0])
        for (int i=1;i<l.size();i++)
        if (l[i]<l[i-1])
        return false;
        else
        continue;
        else if (l[1]<l[0])
        for (int i=1;i<l.size();i++)
        if (l[i]>l[i-1])
        return false;
        else
        continue;
    }
    return true;
}



