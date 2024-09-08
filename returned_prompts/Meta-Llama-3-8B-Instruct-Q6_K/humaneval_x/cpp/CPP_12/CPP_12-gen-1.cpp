    if(strings.empty()) {
        return "";
    }
    string longest = strings[0];
    for(auto i: strings) {
        if(i.length() > longest.length()) {
            longest = i;
        }
    }
    return longest;
}

int main() {
    // Test the function
    vector<string> test = {"a", "bb", "ccc"};
    cout << longest(test) << endl; // Output: "ccc"
    return 0;
}

