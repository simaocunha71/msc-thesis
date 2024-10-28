    vector<string> filtered;
    for (int i=0; i<strings.size(); i++){
        if (strings[i].substr(0,prefix.size()) == prefix){
            filtered.push_back(strings[i]);
        }
    }
    return filtered;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for (int i=0; i<result.size(); i++){
        printf("%s ", result[i].c_str());
    }
    return 0;
}

Answer:
The program filters an input vector of strings only for ones that start with a given prefix.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> filtered;
    for (int i=0; i<strings.size(); i++){
        if (strings[i].substr(0,prefix.size()) == prefix){
            filtered.push_back(strings[i]);
        }
    }
    return filtered;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for (int i=0; i<result.size(); i++){
        printf("%s ", result[i].c_str());
    }
    return 0;
}

This program works by iterating through the input vector and checking if each string starts with the given prefix using the `substr` function. If it does, the string is added to the filtered vector.

In the main function, the `filter_by_prefix` function is called with a vector of strings and a prefix. The result is printed to the console.

The output of this program will be:

abc vector
*/

```

---

### Python Code