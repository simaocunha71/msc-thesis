    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            if(l[i]+l[j]==0){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
    vector<int> v5 = {1};
    printf("%d\n", pairs_sum_to_zero(v1)); // should print 0 (false)
    printf("%d\n", pairs_sum_to_zero(v2)); // should print 0 (false)
    printf("%d\n", pairs_sum_to_zero(v3)); // should print 0 (false)
    printf("%d\n", pairs_sum_to_zero(v4)); // should print 1 (true)
    printf("%d\n", pairs_sum_to_zero(v5)); // should print 0 (false)
    return 0;
}


A: The algorithm you're trying to implement is correct, but it can be optimized. Instead of using a nested loop to traverse the list, you can use a hashing technique that has a time complexity of O(n). Here's how you can do it:

```cpp
bool pairs_sum_to_zero(vector<int> l) {
    unordered_set<int> s;
    for (int i = 0; i < l.size(); i++) {
        if (s.find(-l[i]) != s.end()) {
            return true;
        }
        s.insert(l[i]);
    }
    return false;
}
```

This function works by iterating over the list and checking if the negation of the current element is already in the set. If