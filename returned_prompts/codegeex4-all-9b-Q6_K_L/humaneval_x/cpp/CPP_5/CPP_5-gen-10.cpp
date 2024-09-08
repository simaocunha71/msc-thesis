```cpp
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    vector<int> res;
    if(numbers.size() == 0) return res;
    for(int i = 0; i < numbers.size(); i++){
        res.push_back(numbers[i]);
        if(i != numbers.size() - 1) res.push_back(delimeter);
    }
    return res;
}
```