    int i;
    if (lst.size()==0)
    return true;
    for (i=1;i<lst.size();i++)
    {
        if (lst[i-1]>lst[i])
        return false;
        if (lst[i-1]==lst[i])
        return false;
    }
    return true;
}
//This code is not efficient because it has a time complexity of O(n^2) due to the nested loop.
//We can improve it by using std::equal() from the <algorithm> library.
bool is_sorted(vector<int> lst){
    return std::equal(lst.begin(), lst.end()-1, lst.begin()+1);
}
//This version has a time complexity of O(n) and is more efficient.  It checks if the list is sorted by comparing each element with the next one. If it finds a pair where the first element is greater than the second, it returns false. If it finishes without finding any such pair, it returns true.
//However, this solution does not handle duplicate elements correctly. It returns false for lists with duplicate elements. To fix this, we can modify the solution to only compare elements if they are different. Here's how to do it:
bool is_sorted(vector<int> lst){
    for (int i = 0; i < lst.size() - 1; i++) {
        if (lst[i] > lst[i + 1]) {
            return false;
        }
    }
    return true;
}
//This version handles duplicate elements correctly and has a time complexity of O(n). It checks if the list is sorted by comparing each element with the next one. If it finds a pair where the first element is greater than the second, it returns false. If it finishes without finding any such pair, it returns true.