    vector<int> result;
    if(lst.empty()) return result;
    sort(lst.begin(), lst.end()); // sort the list in ascending order
    result.push_back(lst[0]); // add the smallest element to the result
    lst.erase(lst.begin()); // remove the smallest element from the list
    sort(lst.begin(), lst.end(), greater<int>()); // sort the remaining list in descending order
    result.push_back(lst[0]); // add the largest element to the result
    lst.erase(lst.begin()); // remove the largest element from the list
    while(!lst.empty()) {
        result.push_back(lst[0]); // add the smallest element to the result
        lst.erase(lst.begin()); // remove the smallest element from the list
        sort(lst.begin(), lst.end()); // sort the remaining list in ascending order
    }
    return result;
}

