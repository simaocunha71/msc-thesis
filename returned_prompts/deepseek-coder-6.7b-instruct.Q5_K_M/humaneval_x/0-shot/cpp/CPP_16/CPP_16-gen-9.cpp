    vector<int> count(128, 0);
    for(char& c : str){
        count[tolower(c)] = 1;
    }
    return count_if(begin(count), end(count), [](int i){ return i != 0; });
}

int main(){
    printf("%d\n", count_distinct_characters("xyzXYZ"));
    printf("%d\n", count_distinct_characters("Jerry"));
    return 0;
}
```
The `count_distinct_characters` function works by creating a vector of 128 zeros. 
We then loop through the string and set the corresponding ASCII value to 1. 
Finally, we count the number of elements in the vector that are not zero (i.e., the count of distinct characters). 
The `tolower()` function is used to handle case-insensitivity.

The main function just calls `count_distinct_characters` with two test strings and prints the results.

The time complexity of the function is O(n), where n is the length of the string, because we iterate through the string and the vector once. The space complexity is O(1), because we only use a fixed amount of space to store the counts of the characters, regardless of the input size.

This solution assumes that the string only contains ASCII characters. If the string can contain Unicode characters, the solution would need to be modified to use a map instead of a vector.
*/

//Code:

```C++
#include<stdio.h>
#include<map>
#include<string>
using namespace std;

int count_distinct_characters(string str){ 
    map<char, int> count;
    for(char& c : str){
        count[tolower(c)] = 1;
    }
    return count.size();
}

int main(){
    printf("%d\n", count_distinct_characters("xyzXYZ"));
    printf("%d\n", count_distinct_characters("Jerry"));
    return 0;
}
```

This version of the function works similarly to the previous one,