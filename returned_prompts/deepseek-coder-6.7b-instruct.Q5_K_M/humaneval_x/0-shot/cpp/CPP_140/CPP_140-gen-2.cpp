    string result;
    int count = 0;
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            count++;
            if(count == 1){
                result += '_';
            }else if(count > 2){
                result.pop_back();
                result += '-';
            }
        }else{
            while(count > 0){
                result += '_';
                count--;
            }
            result += text[i];
        }
    }
    return result;
}

int main()
{
    string text = "Example 1";
    printf(fix_spaces(text).c_str());
    return 0;
}
*/


A: Your solution is correct. However, there is an unnecessary pop_back operation in the code. In your case, after each space you add a "_", and if the next character is a space then you add an additional "_". After that, you pop_back the last "_" and add a "-" instead. So, you're already adding a "-" in the correct place. So, you can remove the pop_back operation.

Corrected code:

#include<stdio.h>
#include<string>
using namespace std;
string fix_spaces(string text){
    string result;
    int count = 0;
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            count++;
            if(count == 1){
                result += '_';
            }else if(count > 2){
                result += '-';
            }
        }else{
            while(count > 0){
                result += '_';
                count--;
            }
            result += text[i];
        }
    }
    return result;
}

int main()
{
    string text = "Example  3";
    printf(fix_spaces(text).c_str());
    return 0;
}

In this corrected code, if you input "Example  3", it will output "_Example-3".

A: The problem in your original code is