    vector<int> common_elements;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> intersection;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(intersection, intersection.begin()));
    for (int i = 0; i < intersection.size(); i++)
    {
        common_elements.push_back(intersection[i]);
    }
    sort(common_elements.begin(), common_elements.end());
    return common_elements;
} 