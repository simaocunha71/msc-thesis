    if (lst.size() == 1)
        return true;
    bool is_sorted = true;
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] <= lst[i - 1]) {
            is_sorted = false;
            break;
        }
    }
    return is_sorted && (find(lst.begin(), lst.end(), lst[0]) == lst.end());
}
//Using std::set would also be a correct solution. Here's how you could implement it:

bool is_sorted(vector<int> lst) {
    set<int> s(lst.begin(), lst.end());
    return prev(s.end()) == s.begin();
}
//The std::set will automatically sort the vector, and the prev(s.end()) == s.begin() condition will check if all elements in the set are the same. If they are, it means the original vector was sorted and had no duplicates. If not, it means the vector was not sorted or had duplicates.