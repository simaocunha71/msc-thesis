    if(lst.size()<2) return -1; // return -1 for None
    sort(lst.begin(),lst.end());
    for(int i=1;i<lst.size();i++)
    {
        if(lst[i]>lst[0])
        {
            return lst[i];
        }
    }
    return -1; // return -1 for None
} // end of function


