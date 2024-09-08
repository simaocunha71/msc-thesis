    int count = 0;
    for(int i = 0; i < str.length(); i++){
        count++;
    }
    return count;
}

int main(){
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    cout << "Length of the string is: " << strlen(s) << endl;
    return 0;
}

Answer:
The function strlen is already defined in the standard library of C programming language, it is used to calculate the length of a given string. In this problem, we are going to define our own function strlen to calculate the length of a given string.

The function strlen takes a string as an argument and returns the length of that string. It does this by iterating through each character in the string and incrementing a counter variable until it reaches the end of the string.

In the main function, we ask the user to input a string and then we call our own function strlen with the user's input as an argument. The function returns the length of the string and we print this length to the console.

Here is the complete code:

```cpp
#include<stdio.h>
#include<string>
using namespace std;

int strlen(string str){
    int count = 0;
    for(int i = 0; i < str.length(); i++){
        count++;
    }
    return count;
}

int main(){
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    cout << "Length of the string is: " << strlen(s) << endl;
    return 0;
}
```

The output of this program will be the length of the string entered by the user. For example, if the user enters "hello", the output will be "Length of the string is: 5". The length of the string "hello" is 5 because it has 5 characters: 'h', 'e', 'l', 'l', 'o'.