
The first function is easy to solve using the standard library function next_permutation.  But the problem is that it doesn't solve the problem.  It finds all the permutations of the vector, which is not what we want.  We want to find the next permutation that is larger than the current permutation.  That is, we want to find the next lexicographical permutation.
The algorithm is to find the rightmost element that is smaller than its next element.  We then find the rightmost element that is larger than this element, swap them, and reverse the order of the elements to the right of the first element.  This gives us the next lexicographical permutation.
Here is the code for this function:
bool next_permutation(vector<int>& v) {
    int i = v.size() - 2;
    while (i >= 0 && v[i] >= v[i + 1])
        --i;
    if (i < 0)
        return false;
    int j = v.size() - 1;
    while (v[j] <= v[i])
        --j;
    swap(v[i], v[j]);
    reverse(v.begin() + i + 1, v.end());
    return true;
}

The next function is also easy to solve using the standard library function find_if.  We want to find the first element that is greater than 0, and return the index of that element.  If no such element is found, we return -1.
Here is the code for this function:
int find_positive_index(vector<int>& v) {
    auto it = find_if(v.begin(), v.end(), [](int x) { return x > 0; });
    if (it == v.end())
        return -1;
    return distance(v.begin(), it);
}

The next function is also easy to solve using the standard library function sort.  We want to sort the vector in descending order, and then find the index of the first element that is larger than 0.  If no such element is found, we return -1.
Here is the code for this function:
int find_positive_index_descending(vector<int>& v) {
    sort(v.begin(), v.end(), greater<int>());
    auto it = find_if(v.begin(), v.end(), [](int x) { return x >