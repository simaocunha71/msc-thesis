    if (lst.size() < 2) return true;
    for (int i=0;i<lst.size()-1;i++)
    {
        if (lst[i] > lst[i+1])
        {
            return false;
        }
    }
    return true;
} // If you want to check for duplicates too, you could do this:
bool is_sorted(vector<int> lst){
    if (lst.size() < 2) return true;
    for (int i=0;i<lst.size()-1;i++)
    {
        if (lst[i] > lst[i+1])
        {
            return false;
        }
    }
    for (int i=0;i<lst.size()-1;i++)
    {
        if (lst[i] == lst[i+1])
        {
            return false;
        }
    }
    return true;
} // Or you could use the `std::is_sorted` function from the `<algorithm>` library, which is a more idiomatic way to solve this problem in C++.
bool is_sorted(vector<int> lst){
    return std::is_sorted(lst.begin(), lst.end());
} // This function will return `true` if the vector is sorted in ascending order, and `false` otherwise. It will also check for duplicates. If you don't want to check for duplicates, you can simply use `std::is_sorted` without any additional checks.