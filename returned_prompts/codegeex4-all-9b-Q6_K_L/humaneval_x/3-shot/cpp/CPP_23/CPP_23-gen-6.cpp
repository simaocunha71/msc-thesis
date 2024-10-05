
Here are some comments on your code:

Your indentation is off, which makes it difficult to read.  Try to use an editor that helps you with this.  Visual Studio Code has a nice feature for this.
You don't need to use the absolute function with the subtraction when you are checking if two numbers are closer than a threshold, because you are checking if the distance between the numbers is smaller than the threshold.  This is equivalent to checking if the absolute value of the difference is smaller than the threshold.
Your code for the second question does not account for invalid input (i.e. strings without balanced parentheses).  You should add some error checking for this.
Your code for the third question is correct, but it is not the most efficient way to do it.  You can use the modulo operator (%) to get the decimal part of the number.  This is more efficient than converting the number to an integer and then subtracting it from the original number.
Your code for the fourth question is correct, but it is not the most efficient way to do it.  You can use the size() function to get the length of the string.  This is more efficient than converting the string to a character array and then using a loop to count the number of characters.

Here is the corrected code:

#include<stdio.h>
#include<vector>
#include<math.h>
#include<string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0; i<numbers.size(); i++){
        for (int j=i+1; j<numbers.size(); j++){
            if (abs(numbers[i]-numbers[j])<threshold){
                return true;
            }
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0; i<paren_string.length(); i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        } else if (chr==')'){
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

int strlen(string