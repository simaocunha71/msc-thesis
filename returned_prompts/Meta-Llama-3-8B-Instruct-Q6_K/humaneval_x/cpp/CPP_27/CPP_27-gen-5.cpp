    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z'){
            str[i]-=32;  // convert lowercase to uppercase
        }
        else if(str[i]>='A' && str[i]<='Z'){
            str[i]+=32;  // convert uppercase to lowercase
        }
    }
    return str;
}
int main(){
    string str = "Hello";
    cout<<filp_case(str)<<endl;
    return 0;
}

Output:
hELLO

Explanation:
In this program, we are iterating over each character in the given string. If the character is in lowercase (i.e., its ASCII value is between 'a' and 'z'), we subtract 32 to convert it to uppercase. If the character is in uppercase (i.e., its ASCII value is between 'A' and 'Z'), we add 32 to convert it to lowercase. Finally, we return the modified string. In the main function, we call the filp_case function with the string "Hello" and print the result. The output is "hELLO". 

Note: This program assumes that the input string contains only English alphabets. It will not work correctly for other characters. For a more robust solution, you can use the tolower and toupper functions from the cctype library. 

Also, note that this program modifies the original string. If you want to keep the original string unchanged, you should create a copy of the string at the beginning of the function. 

Here is the modified version of the program that keeps the original string unchanged:

```c++
#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string flip_case(string str) {
    string result = str; // Create a copy of the original string
    for(int i=0;i<result.length();i++){
        if(result[i]>='a' && result[i]<='z'){
            result[i]-=32;  // convert lowercase to uppercase
        }
        else if(result[i]>='A' && result[i]<='Z'){
            result[i]+=32;  // convert uppercase to lowercase
        }
    }
    return result;
}

int main(){
    string str = "Hello";
    cout<<flip_case(str)<<endl;
    return 0;
}
```  */ 

Output:
hELLO
```  */  ```  ```  ```  ```  ```  ```  ``` 