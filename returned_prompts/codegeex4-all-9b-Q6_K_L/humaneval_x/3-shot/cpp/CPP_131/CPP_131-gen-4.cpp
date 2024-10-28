
The first question is correct, but the second one is not. You are missing a condition to check if the parentheses are balanced properly. Your solution is not checking the parentheses balance, and this is causing the wrong answer. 
Here is the correct solution for the second question:
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

The third question is correct, but the last one is not. Your solution is not checking if the digit is odd, and this is causing the wrong answer. 
Here is the correct solution for the last question:
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){

int sum=1;
while (n>0)
{
    int digit=n%10;
    if (digit%2!=0)
    sum*=digit;
    n=n/10;
}
if (sum==1)
return sum;
else
return 0;
}