Looks like your code is mostly correct, but you're missing a return statement in the last function. Here it is:

```cpp
vector<string> by_length(vector<int> arr){
    vector<string> words{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    map<int, string> m;
    for(int i=1; i<=9; i++)
        m[i] = words[i];
    vector<int> v;
    for(int i=0; i<arr.size(); i++)
        if(arr[i]>=1 && arr[i]<=9)
            v.push_back(arr[i]);
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    vector<string> result;
    for(int i=0; i<v.size(); i++)
        result.push_back(m[v[i]]);
    return result;
}
```

This function works by first creating a map of integers to their corresponding word representations, then creating a new vector of the integers between 1 and 9 (inclusive) found in the input array.