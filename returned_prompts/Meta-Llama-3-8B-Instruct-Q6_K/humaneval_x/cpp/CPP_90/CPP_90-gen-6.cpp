    if(lst.size()==0)
        return NULL;
    sort(lst.begin(),lst.end());
    if(lst.size()==1)
        return NULL;
    else
        return lst[1];
}

