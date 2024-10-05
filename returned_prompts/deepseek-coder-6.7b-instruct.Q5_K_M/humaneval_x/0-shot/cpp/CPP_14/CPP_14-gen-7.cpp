    vector<string> result;
    for(int i = 0; i < str.length(); i++){
B:
        result.push_back(str.substr(0, i + 1));
    }
    return result;
}

int main() {
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes) {
        printf("%s\n", prefix.c_str());
    }
    return 0;
}

*/

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

vector<string> all_prefixes(string str){
    vector<string> result;
    for(int i = 0; i < str.length(); i++){
        result.push_back(str.substr(0, i + 1));
    }
    return result;
}

int main() {
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes) {
        printf("%s\n", prefix.c_str());
    }
    return 0;
}

// Explanation:
// The function all_prefixes takes a string as input and returns a vector of strings.
// It starts by creating an empty vector of strings.
// Then it goes through each character in the input string. For each character, it creates a substring from the start of the string up to the current character (inclusive) and adds this substring to the vector.
// Finally, it returns the vector.
// The main function tests this by calling all_prefixes with the string "abc", prints each prefix on a new line, and returns 0 to indicate success.

// This code is written in C++ and uses the standard library. It uses the substr function to create substrings, and the push_back function to add elements to a vector.

// The time complexity of this code is O(n^2), where n is the length of the input string. This is because for each character in the string, it creates a substring which takes O(n) time, and it does this n times. The space complexity is O(n^2), as in the worst case (