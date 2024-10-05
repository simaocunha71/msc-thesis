    if (lst.size()==0 || lst.size()==1)
    return true;
    if (lst[0]>=lst[1])
    return false;
    return (lst[i]==lst[i+1] || is_sorted(vector<int>(lst.begin()+1,lst.begin()+i+1)))&& is_sorted(vector<int>(lst.begin()+i+1,lst.end()));
}



