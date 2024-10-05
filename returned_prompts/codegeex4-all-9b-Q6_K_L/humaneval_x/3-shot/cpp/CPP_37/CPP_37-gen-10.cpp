
The first question is pretty straight-forward. The second one requires careful handling of parenthesis. For the third one, you can use the modulus operator to find out the remainder of the division. The final question requires a bit of thought, but it can be solved using a simple loop and the sort() function from the algorithm library.
Here are the solutions:
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size()-1;i++)
    for (int j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;
    return false;
}
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
        level+=1;
        current_paren+=chr;
        }
        if (chr==')'){
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
float truncate_number(float number){
    return number-int(number);
}
vector<float> sort_even(vector<float> l){
    vector<float> even_values;
    for (int i=0;i<l.size();i+=2)
        even_values.push_back(l[i]);
    sort(even_values.begin(),even_values.end());
    for (int i=0;i<l.size();i+=2)
        l[i]=even_values[i/2];
    return l;
}