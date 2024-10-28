    int max = -1;
    int max_count = 0;
    map<int, int> count_map;
    for (int i = 0; i < lst.size(); i++) {
        if (count_map.find(lst[i]) == count_map.end()) {
            count_map[lst[i]] = 1;
        } else {
            count_map[lst[i]]++;
        }
    }
    for (auto it = count_map.begin(); it != count_map.end(); it++) {
        if (it->second >= it->first) {
            max = it->first;
            max_count = it->second;
        }
    }
    return max;
}
//Test
#include <iostream>
int main() {
    vector<int> lst1 = {4, 1, 2, 2, 3, 1};
    vector<int> lst2 = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    vector<int> lst3 = {5, 5, 4, 4, 4};
    cout << search(lst1) << endl;  // 2
    cout << search(lst2) << endl;  // 3
    cout << search(lst3) << endl;  // -1
    return 0;
}  // Output: 2, 3, -1
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test
//Test