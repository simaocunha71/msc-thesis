    if(lst.size()<2)
    return true;
    int prev=lst[0];
    for (int i=1;i<lst.size();i++)
    {
        if (lst[i]<prev)
        return false;
        prev=lst[i];
    }
    return true;
} // This function will return false if there are duplicate numbers in the list


