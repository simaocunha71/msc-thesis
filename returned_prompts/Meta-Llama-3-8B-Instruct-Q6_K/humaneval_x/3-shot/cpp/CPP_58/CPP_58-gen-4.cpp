    vector<int> result;
    set<int> set1(l1.begin(), l1.end());
    set<int> set2(l2.begin(), l2.end());
    set<int> common_elements;
    set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                     inserter(common_elements, common_elements.begin()));
    for (set<int>::iterator it = common_elements.begin(); it != common_elements.end(); ++it)
    {
        result.push_back(*it);
    }
    sort(result.begin(), result.end());
    return result;
} 



