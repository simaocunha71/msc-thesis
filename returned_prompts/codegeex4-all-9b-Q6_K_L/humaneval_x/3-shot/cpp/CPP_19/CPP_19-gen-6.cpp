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

The code is fine, but here's a more C++ way to handle the string and character extraction.
#include<vector>
#include<string>
#include<sstream>

using namespace std;

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;

    stringstream ss(paren_string);

    for(char c; ss >> c;)
    {
        if (