```cpp
vector<int> sort_third(vector<int> l) {
    vector<int> divisible_by_three;
    for (int i = 2; i < l.size(); i += 3) {
        divisible_by_three.push_back(l[i]);
    }
    sort(divisible_by_three.begin(), divisible_by_three.end());
    int j = 0;
    for (int i = 2; i < l.size(); i += 3) {
        l[i] = divisible_by_three[j++];
    }
    return l;
}
```