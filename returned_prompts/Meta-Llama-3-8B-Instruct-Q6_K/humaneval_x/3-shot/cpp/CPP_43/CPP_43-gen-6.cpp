    sort(l.begin(), l.end());
    int i,j;
    for (i=0;i<l.size();i++)
    for (j=i+1;j<l.size();j++)
    if (l[i]+l[j]==0)
    return true;

    return false;
} 
//Note: This function can be optimized by using a set instead of a sorted vector, as the problem statement ensures that the input vector contains distinct elements. This would reduce the time complexity from O(n^2) to O(n). Also, as the problem statement doesn't guarantee the input vector contains at least two elements, we should add a check for this before starting the loop.
//Here is the optimized function:
bool pairs_sum_to_zero(vector<int> l){
    set<int> s(l.begin(), l.end());
    for (auto it = s.begin(); it != s.end(); ++it) {
        int complement = -(*it);
        if (s.find(complement) != s.end()) {
            return true;
        }
    }
    return false;
}  // Time Complexity O(n) where n is the number of elements in the input vector. 

