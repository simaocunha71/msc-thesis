    vector<int> result;
    for(int i : numbers)
    {
        if(find(result.begin(), result.end(), i) == result.end())
        {
            result.push_back(i);
        }
    }
    return result;
} // or using set
vector<int> remove_duplicates(vector<int> numbers){
    set<int> s;
    for(int i : numbers)
    {
        s.insert(i);
    }
    vector<int> result(s.begin(), s.end());
    return result;
}
} // using set unordered_set
vector<int> remove_duplicates(vector<int> numbers){
    unordered_set<int> s;
    for(int i : numbers)
    {
        s.insert(i);
    }
    vector<int> result(s.begin(), s.end());
    return result;
} // or using map
vector<int> remove_duplicates(vector<int> numbers){
    map<int, int> m;
    for(int i : numbers)
    {
        if(m.find(i) == m.end())
        {
            m[i] = 1;
        }
    }
    vector<int> result;
    for(map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        result.push_back(it->first);
    }
    return result;
} // or using unordered_map
vector<int> remove_duplicates(vector<int> numbers){
    unordered_map<int, int> m;
    for(int i : numbers)
    {
        if(m.find(i) == m.end())
        {
            m[i] = 1;
        }
    }
    vector<int> result;
    for(unordered_map<int, int>::iterator it = m.begin(); it != m.end(); it++)
    {
        result.push_back(it->first);
    }
    return result;
} // or using sort and unique
vector<int> remove_duplicates(vector<int> numbers){
    sort(numbers.begin(), numbers.end());
    numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());
    return numbers;
} // or using set_difference
vector<int> remove_duplicates(vector<int> numbers){
    set<int> s(numbers.begin(), numbers.end());
    vector<int> result(s.begin(), s.end());
    return result;
}
} // using set_difference
vector<int> remove_duplicates(vector<int> numbers){
    set<int> s;
    set_difference(numbers.begin(), numbers.end(), s.begin(), s.end());
    vector<int> result(s.begin(), s.end());
    return result;
} // using set_intersection
vector<int> remove_duplicates(vector<int> numbers){
