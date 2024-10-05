
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
}

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

float truncate_number(float number){
    return number-int(number);
}

map<char,int> histogram(string test){
    map<char,int> test_map;

    for (int i=0;i<test.length();i++)
    {
        test_map[test[i]]+=1;
    }

    return test_map;
}

int main()
{
    printf("%s",has_close_elements({1.0, 2.0, 3.0}, 0.5)?"true":"false");
    printf("%s",has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)?"true":"false");

    separate_paren_groups("( ) (( )) (( )( ))");

    printf("%s",truncate_number(3.5));

    histogram("a b c");

    return 0;
}