    if(strings.empty()) {
        return "";
    }
    string longest_str = strings[0];
    for(int i = 1; i < strings.size(); i++) {
        if(strings[i].size() > longest_str.size()) {
            longest_str = strings[i];
        }
    }
    return longest_str;
}

int main() {
    vector<string> v = {"a", "b", "c", "ccc", "bb"};
    cout << longest(v) << endl;
    return 0;
}

Output:
ccc
Explanation: The longest string in the given vector is "ccc". The function will return the first string in case of multiple strings of the same length, so it will return "ccc" in this case. If the input vector is empty, it will return an empty string. If the input vector contains only one string, it will return that string. It will iterate through the vector and find the longest string, returning it. If no strings are present, it will return an empty string. It will work as expected for any input vector of strings.