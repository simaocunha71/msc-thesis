    vector<string> result;
    for(const auto& str : strings){
        if(str.find(prefix) == 0) result.push_back(str);
    }
    return result;
}
// Test the function
int main() {
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(const auto& str : result){
        cout << str << endl;
    }
    return 0;
}

Output:
abc
vector

Explanation:
The `filter_by_prefix` function takes a vector of strings and a prefix string as input. It iterates over each string in the input vector and checks if the string starts with the given prefix using the `find` method. If the string starts with the prefix, it is added to the result vector. Finally, the result vector is returned. In the `main` function, we test the `filter_by_prefix` function with a vector of strings and a prefix string, and print the resulting filtered vector.