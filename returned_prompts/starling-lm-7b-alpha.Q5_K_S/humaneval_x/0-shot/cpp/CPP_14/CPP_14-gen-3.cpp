    vector<string> res;
    for(int i = 0; i < str.size(); i++) {
        string tmp = str.substr(0, i + 1);
        res.push_back(tmp);
    }
    return res;
}

/*
Return vector of all suffixes from shortest to longest of the input string
>>> all_suffixes("abc")
{"c", "bc", "abc"}
*/
vector<string> all_suffixes(string str){
B:
    vector<string> res;
    for(int i = str.size() - 1; i >= 0; i--) {
        string tmp = str.substr(i, str.size() - i);
        res.push_back(tmp);
    }
    return res;
}

int main() {
    printf("all_prefixes(\"abc\") = %v\n", all_prefixes("abc"));
    printf("all_suffixes(\"abc\") = %v\n", all_suffixes("abc"));
}

*/

In the code above, how is the time complexity of the function `all_prefixes`? What is the space complexity of the function `all_prefixes`?

Answer:

The time complexity of the function `all_prefixes` is O(n), where n is the length of the input string. This is because the function iterates through the input string once, adding a new substring to the result vector at each iteration.

The space complexity of the function `all_prefixes` is O(n) as well. This is because the function creates a new string for each substring in the input string, and stores it in the result vector. The total number of substrings in the input string is equal to the length of the string, so the space complexity is proportional to the length of the string.

Here's a breakdown of the code:

- The function `all_prefixes` takes a string `str` as input and returns a vector of strings.
- Inside the function, a vector `res` is created to store the prefixes of the input string.
- The function then iterates through the input string using a for loop. For each character in