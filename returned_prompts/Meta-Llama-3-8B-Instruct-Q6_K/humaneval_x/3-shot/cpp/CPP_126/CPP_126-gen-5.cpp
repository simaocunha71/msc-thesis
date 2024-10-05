    if (lst.size()==1 || lst.size()==2)
    return true;
    for (int i=1;i<lst.size();i++)
    {
        if (lst[i-1]>lst[i])
        return false;
    }
    if (any_of(lst.begin(), lst.end(), [i](int x){return count(lst.begin(), lst.end(), x)>1;}))
    return false;
    return true;
} // This function is used to check if the list contains duplicate elements.
bool has_duplicates(vector<int> lst){
    for(int i=0; i<lst.size(); i++)
    {
        for(int j=i+1; j<lst.size(); j++)
        {
            if(lst[i] == lst[j])
                return true;
        }
    }
    return false;
} // The main function checks for sorting and duplicates.
bool is_sorted(vector<int> lst){
    if (lst.size()==1 || lst.size()==2)
        return true;
    for (int i=1; i<lst.size(); i++)
    {
        if (lst[i-1] > lst[i])
            return false;
    }
    if(has_duplicates(lst))
        return false;
    return true;
} // This function checks if the list is sorted in ascending order. It also checks for duplicate elements.
bool is_sorted(vector<int> lst){
    if (lst.size()==1 || lst.size()==2)
        return true;
    for (int i=1; i<lst.size(); i++)
    {
        if (lst[i-1] > lst[i])
            return false;
    }
    return true;
} // This function checks if the list is sorted in ascending order. It does not check for duplicate elements. 
bool is_sorted(vector<int> lst){
    return is_sorted(lst);
} // This function is a simple recursion. It checks if the list is sorted in ascending order. It does not check for duplicate elements. 
bool is_sorted(vector<int> lst){
    if (lst.size()==1)
        return true;
    for (int i=1; i<lst.size(); i++)
    {
        if (lst[i-1] > lst[i])
            return false;
    }
    return is_sorted(vector<int>(lst.begin()+1, lst.end()));
} // This function is a simple recursion. It checks if the list is sorted in ascending order. It does not check for duplicate elements. 
bool is_sorted(vector<int> lst){
    if (lst