
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
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

#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number-int(number);
}

#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string result;
    int lena=a.length();
    int lenb=b.length();
    int i;
    for (i=0;i<lenb;i++)
    {
        if (a[i]=='1'&&b[i]=='1')
            result+='0';
        if (a[i]=='0'&&b[i]=='0')
            result+='0';
        if (a[i]=='1'&&b[i]=='0')
            result+='1';
        if (a[i]=='0'&&b[i]=='1')
            result+='1';
    }
    return