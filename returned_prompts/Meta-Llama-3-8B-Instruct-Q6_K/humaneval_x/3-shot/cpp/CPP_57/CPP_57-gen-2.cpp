    bool increasing=true;
    bool decreasing=true;
    for (int i=1;i<l.size();i++)
    {
        if (l[i-1]>l[i])
        {
            increasing=false;
        }
        if (l[i-1]<l[i])
        {
            decreasing=false;
        }
    }
    return increasing || decreasing;
}  // this function is not working correctly. it does not handle the case when the vector has less than two elements.
// also, it does not handle the case when the vector is empty. // it also does not check if the vector contains only one element. in that case, we should return true, as the vector is both increasing and decreasing.  // we should also return true if the vector is empty or has only one element. 
bool monotonic(vector<float> l){
    if (l.size()<=1)
        return true;
    bool increasing=true;
    bool decreasing=true;
    for (int i=1;i<l.size();i++)
    {
        if (l[i-1]>l[i])
        {
            increasing=false;
        }
        if (l[i-1]<l[i])
        {
            decreasing=false;
        }
    }
    return increasing || decreasing;
} // this function still does not handle the case when the vector is empty. we should add a condition to check if the size of the vector is 0 before the loop. 
bool monotonic(vector<float> l){
    if (l.size()<=1)
        return true;
    if (l.size()==0)
        return true;
    bool increasing=true;
    bool decreasing=true;
    for (int i=1;i<l.size();i++)
    {
        if (l[i-1]>l[i])
        {
            increasing=false;
        }
        if (l[i-1]<l[i])
        {
            decreasing=false;
        }
    }
    return increasing || decreasing;
} // this function should now correctly handle all cases. it returns true for empty, single element and increasing/decreasing vectors, and false for vectors that are neither increasing nor decreasing.  // we should also consider the case when the vector contains only one element, in that case we should return true. 
bool monotonic(vector<float> l){
    if (l.size()<=1)
        return true;
    if (l.size()==0)
        return true;
    bool increasing=true;
    bool decreasing=true;
    for (int i=1;i<l.size();i++)
