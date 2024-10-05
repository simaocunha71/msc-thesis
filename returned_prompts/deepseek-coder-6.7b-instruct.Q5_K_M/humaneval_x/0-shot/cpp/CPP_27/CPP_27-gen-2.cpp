    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z')
            str[i] = str[i] - 32;
        else if(str[i]>='A' && str[i]<='Z')
            str[i] = str[i] + 32;
    }
    return str;
}

int main(){
    string str;
    printf("Enter a string: ");
    getline(cin,str);
    str = filp_case(str);
    printf("Flipped string: %s", str.c_str());
    return 0;
}

This program uses C++ language to solve the problem. It reads a string from the user, then it uses a loop to go through each character of the string. If the character is a lowercase letter, it is converted to uppercase by subtracting 32 from its ASCII value. If the character is an uppercase letter, it is converted to lowercase by adding 32 to its ASCII value. The resulting string is then printed on the screen.
*/
#include<iostream>
#include<string>
using namespace std;
string filp_case(string str){
    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z')
            str[i] = str[i] - 32;
        else if(str[i]>='A' && str[i]<='Z')
            str[i] = str[i] + 32;
    }
    return str;
}

int main(){
    string str;
    cout<<"Enter a string: ";
    getline(cin,str);
    str = filp_case(str);
    cout<<"Flipped string: "<<str;
    return 0;
}

This program does the same thing as the previous one but uses C++ iostream library to handle input and output.
*/

/*
