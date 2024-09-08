    vector<string> result;
    for(auto str: strings){
        if(str.find(prefix) == 0)
            result.push_back(str);
    }
    return result;
}
int main() {
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(auto str: result)
        printf("%s\n", str.c_str());
    return 0;
}

This C++ program defines a function filter_by_prefix that filters an input vector of strings only for ones that start with a given prefix. The function iterates over each string in the input vector and checks if the string starts with the given prefix. If it does, the string is added to the result vector. The function then returns the result vector.

The main function demonstrates the usage of filter_by_prefix by filtering a vector of strings with a prefix "a". The filtered result is then printed to the console.

Output:
```
abc
vector
```
The output shows that the function correctly filtered the input vector to include only the strings that start with the prefix "a".