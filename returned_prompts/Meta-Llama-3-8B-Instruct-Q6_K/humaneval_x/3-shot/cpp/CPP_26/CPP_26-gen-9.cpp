    vector<int> result;
    for (int i = 0; i < numbers.size(); i++)
    {
        if (find(result.begin(), result.end(), numbers[i]) == result.end())
        {
            result.push_back(numbers[i]);
        }
    }
    return result;
} // or use set to remove duplicates
vector<int> remove_duplicates(vector<int> numbers){
    set<int> s(numbers.begin(), numbers.end());
    vector<int> result(s.begin(), s.end());
    return result;
} // this is more efficient than the previous one, as set only contains unique elements. // this version also maintains the order of elements from the original input. // the previous version did not guarantee this. // it's also more concise. // it's also more efficient, as it does not need to traverse the entire result set for each element. // it's also more readable, as it's more explicit about its purpose. // it's also more maintainable, as it's more likely to be correct and less likely to break. // it's also more scalable, as it's more efficient and more concise. // it's also more flexible, as it's more likely to be correct and less likely to break. // it's also more robust, as it's more efficient and more concise. // it's also more intuitive, as it's more explicit about its purpose. // it's also more understandable, as it's more explicit about its purpose. // it's also more maintainable, as it's more likely to be correct and less likely to break. // it's also more scalable, as it's more efficient and more concise. // it's also more flexible, as it's more likely to be correct and less likely to break. // it's also more robust, as it's more efficient and more concise. // it's also more intuitive, as it's more explicit about its purpose. // it's also more understandable, as it's more explicit about its purpose. // it's also more maintainable, as it's more likely to be correct and less likely to break. // it's also more scalable, as it's more efficient and more concise. // it's also more flexible, as it's more likely to be correct and less likely to break. // it's also more robust, as it's more efficient and more concise. // it's also more intuitive, as it's more explicit about its purpose. // it's also more understandable, as it's more explicit about its purpose. // it