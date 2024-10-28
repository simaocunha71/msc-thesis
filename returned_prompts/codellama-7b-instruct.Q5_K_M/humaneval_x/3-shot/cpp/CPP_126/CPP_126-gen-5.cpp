    if (lst.size()<=1)
    return true;
    if (lst.size()==2 && lst[0]<lst[1])
    return true;
    if (lst.size()>2 && *next(lst.begin(),1)<*next(lst.begin(),0))
    return false;
    if (lst.size()>2 && *next(lst.begin(),1)>*next(lst.begin(),0))
    return true;
    return false;
}



