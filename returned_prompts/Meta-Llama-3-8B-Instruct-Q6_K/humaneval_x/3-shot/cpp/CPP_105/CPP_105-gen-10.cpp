    vector<string> res;
    map<int, string> num_to_word = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    vector<int> sorted_arr;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            sorted_arr.push_back(i);
        }
    }
    sort(sorted_arr.begin(), sorted_arr.end());
    reverse(sorted_arr.begin(), sorted_arr.end());
    for (int i : sorted_arr) {
        res.push_back(num_to_word[i]);
    }
    return res;
}
```



### 1. Check if in given vector of numbers, are any two numbers closer to each other than given threshold.
```
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}
```
This function checks if there are any two numbers in the given vector that are closer to each other than the given threshold. It uses a nested loop to iterate over all pairs of numbers in the vector and checks if the absolute difference between the two numbers is less than the threshold. If it finds such a pair, it returns true. If it doesn't find any such pair after checking all pairs, it returns false.

### 2. Separate groups of nested parentheses in a string.
```
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren