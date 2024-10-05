
Q1: The first question is a bit ambiguous. The comment says "Check if in given vector of numbers, are any two numbers closer to each other than given threshold." However, the code checks for any two numbers that are further apart than the threshold. If you want to check if any two numbers are closer than the threshold, you need to change the return value to false and the if statement to if (abs(numbers[i]-numbers[j])>threshold). Also, the code is missing the header file for the vector and math.h.
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])>threshold)
                return true;
    return false;
}

Q2: The second question is also a bit ambiguous. The comment says "Separate groups are balanced (each open brace is properly closed) and not nested within each other Ignore any spaces in the input string." However, the code does not ignore spaces. Also, the code is missing the header file for the string.
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
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

Q3: The third question is also a bit ambiguous. The comment says "Return the decimal part of the number." However, the code returns the fractional part of the number. Also, the code is missing the header file for math.h.
#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number-int(number);
}

Q4: The fourth question is also a bit ambiguous