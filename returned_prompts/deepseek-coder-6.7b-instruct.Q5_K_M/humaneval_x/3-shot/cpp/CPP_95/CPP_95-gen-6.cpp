The code you've written is almost correct, but you seem to be missing some required parts. Here's the corrected versions of your functions:

Q1:
```cpp
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){

    for  (int i = 0; i < numbers.size(); i++)
        for  (int j = i+1; j < numbers.size(); j++)
            if  (abs(numbers[i]-numbers[j]) < threshold)
                return true;
    return false;
}
```

Q2:
```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){

    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (unsigned int i = 0; i < paren_string.length(); i++){
        chr = paren_string[i];
        if (chr == '('){
            level += 1;
            current_paren += chr;
        }
        if (chr == ')'){
            level -= 1;
            current_paren += chr;
            if (level == 0){
                all_