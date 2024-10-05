    if (n==0 || n==1)
    return 0;
    if (n==2)
    return 1;
    int a=0,b=0,c=1;
    for (int i=3;i<=n;i++)
    {
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
    }
    return c;
}#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for(i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if(chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if(chr==')')
        {
            level-=1;
            current_paren+=chr;
            if(level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for(i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if(chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if(chr==')')
        {
            level-=1;
            current_paren+=chr;
            if(level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}
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
    for(i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if(chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if(chr==')')
        {
            level-=1;
            current_paren+=chr;
            if(level==