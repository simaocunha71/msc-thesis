
The first one is correct, although it could be more efficient to break out of the loop early if you find two numbers that are close enough.
The second one has a bug.  The code doesn't handle the case where there is a string of spaces at the end of the input string.  The third one is correct.  The fourth one isn't working because you are using the string constructor to create a string from a character.  You should use the string concatenation operator instead.  Here's a corrected version:
#include<stdio.h>
#include<string>
using namespace std;
string fix_spaces(string text){

    string result="";
    string last="";
    string current="";
    int i;
    int count=0;
    for (i=0;i<text.length();i++)
    {
        current=text[i];
        if (current==' ')
        {
            count+=1;
            if (count==2)
            {
                result=result+'-';
            }
        }
        else
        {
            if (count==1)
            {
                result=result+'_';
            }
            else if (count>2)
            {
                result=result+'-';
            }
            count=0;
            result=result+current;
        }
    }
    return result;
}