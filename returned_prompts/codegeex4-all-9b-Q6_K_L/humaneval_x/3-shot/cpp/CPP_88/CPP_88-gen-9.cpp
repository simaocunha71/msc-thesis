
The first problem is in your first function, you are not declaring the variables i and j before the loops.
Second, the second function is a bit confusing, especially if you do not know the string class. I would suggest you to use the string::find and string::substr functions. It will be much easier.
Third, in the third function, I would suggest you to use the fmod function from cmath.
Fourth, in your fourth function, you are not copying the array before sorting it. You should use the std::copy function or the std::vector::assign method.
Here is the corrected code:
#include<stdio.h>
#include<vector>
#include<math.h>
#include<string>
#include<algorithm>
#include<cmath>

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
    return fmod(number, 1);
}

vector<int> sort_array(vector<int> array){
    int sum=array[0]+array[array.size()-1];
    if (sum%2==0)
    sort(array.begin(), array.end(), greater<int>());
    else
    sort(array.begin(), array.end());
    return array;
}