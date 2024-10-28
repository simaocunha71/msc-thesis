
Q1:
Your solution has a major flaw. You are using a nested for loop, which makes it O(n^2) in time complexity. You can solve this in O(n) by using a single for loop and keeping track of the minimum and maximum values in the array. If the difference between the maximum and minimum is less than the threshold, return true. Otherwise, return false.
Here's the modified code:
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    float min_val = numbers[0];
    float max_val = numbers[0];
    for(int i=1; i<numbers.size(); i++){
        if(numbers[i] < min_val){
            min_val = numbers[i];
        }
        if(numbers[i] > max_val){
            max_val = numbers[i];
        }
    }
    if(max_val - min_val < threshold){
        return true;
    }
    return false;
}

Q2:
Your solution is correct. You are using a single for loop and keeping track of the current level and the current paren string. If the level becomes 0, you add the current paren string to the all_parens vector and reset the current paren string. Otherwise, you add the current character to the current paren string. Finally, you return the all_parens vector.
Here's the modified code:
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
                current_paren="";
            }
        }
    }
    return all_parens;
}

Q3:
Your solution is incorrect. You are using the pow() function from the math library, which is not the correct way to calculate powers modulo p. Instead, you should use the fast exponentiation algorithm, which is more efficient and correct. Here's the modified code:
