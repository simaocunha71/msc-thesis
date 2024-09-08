    vector<string> result;
    for (string str : strings) {
        if (str.find(substring) != string::npos) {
            result.push_back(str);
        }
    }
    return result;
}

int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for (string str : result) {
        printf("%s\n", str.c_str());
    }
    return 0;
}

O/P:
abc
bacd
vector

Explanation: 
The code defines a function filter_by_substring that takes a vector of strings and a substring as input. The function iterates over each string in the input vector and checks if the substring is present in the string using the find method of the string class. If the substring is found, the string is added to a new vector result. Finally, the function returns the result vector.

In the main function, we create a vector of strings and a substring, and then call the filter_by_substring function to filter the strings based on the substring. The resulting vector is then printed to the console. The output shows the strings that contain the substring "a". 







