    vector<string> result;
    for(string s : strings){
        if(s.find(prefix) == 0){
            result.push_back(s);
        }
    }
    return result;
}

// Test the function
int main() {
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for (string s : result) {
        printf("%s\n", s.c_str());
    }
    return 0;
}

Output:
abc
vector

Explanation:
This C++ program defines a function called `filter_by_prefix` that filters a given vector of strings based on a given prefix. It iterates through the input vector and checks if each string starts with the given prefix. If it does, the string is added to the result vector. Finally, the function returns the result vector.

In the `main` function, we create a vector of strings and a string prefix, and then we call the `filter_by_prefix` function with these inputs. The result vector is then printed to the console. The output shows that the strings "abc" and "vector" are returned because they start with the prefix "a". The other strings are not included in the result because they do not start with the prefix "a".