    for(int i = 0; i < str.length(); i++)
    {
        if(islower(str[i]))
        {
            str[i] = toupper(str[i]);
        }
        else if(isupper(str[i]))
        {
            str[i] = tolower(str[i]);
        }
    }
    return str;
}
int main()
{
    string str = "Hello";
    printf("%s\n",filp_case(str).c_str());
    return 0;
}



ANSWER:
/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string filp_case(string str){
    for(int i = 0; i < str.length(); i++)
    {
        if(islower(str[i]))
        {
            str[i] = toupper(str[i]);
        }
        else if(isupper(str[i]))
        {
            str[i] = tolower(str[i]);
        }
    }
    return str;
}
int main()
{
    string str = "Hello";
    printf("%s\n",filp_case(str).c_str());
    return 0;
}




































































































































































