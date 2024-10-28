
This is a good start.  Your code looks clean and well-structured.  Here are a few suggestions that will improve it:

Avoid using namespace std;  It's considered bad practice.  The namespace std is large and contains many names that are not relevant to your program.  It's best to avoid using it at all, or only in a small scope.
Remove the comment in the first function.  It's not necessary and is cluttering up the code.
In the second function, you could use the string::find function to find the start and end of each group of parentheses.
In the third function, you could use the math.h library's fmod function to get the decimal part of the number.
In the fourth function, you could use the std::accumulate function to get the sum of all the numbers in the vector.  This would make your code more concise and easier to read.

Here's the modified code:

#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
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
    return number - int(number);
}

long long minSubArraySum(vector<long long> nums){
    long long min_sum = *min_element(nums.begin(), nums.end());
    return min_sum