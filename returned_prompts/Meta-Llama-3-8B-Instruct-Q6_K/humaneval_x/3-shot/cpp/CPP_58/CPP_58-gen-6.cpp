    set<int> set1(l1.begin(), l1.end());
    set<int> set2(l2.begin(), l2.end());
    set<int> common_set;
    set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), 
                     inserter(common_set, common_set.begin()));
    vector<int> result(common_set.begin(), common_set.end());
    sort(result.begin(), result.end());
    return result;
} // using set_intersection function from algorithm library
// http://www.cplusplus.com/reference/algorithm/set_intersection/
// http://www.cplusplus.com/reference/vector/vector/operator%3D%3D/ 
// http://www.cplusplus.com/reference/algorithm/sort/ 
// http://www.cplusplus.com/reference/set/set/begin/
// http://www.cplusplus.com/reference/set/set/insert/

