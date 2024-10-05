
The first problem is that you have not included the math.h library.
The second problem is that you are missing the include statement for the iostream library.  This is necessary to use cin and cout.  I have included this in my version of the code below.  Also, I added the main function which will allow the code to run.
Here is your first code with the necessary libraries included and the main function added:
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;
    return false;
}

int main()
{
    vector<float> num1={1.0, 2.0, 3.0};
    vector<float> num2={1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    cout<<has_close_elements(num1, 0.5)<<endl;
    cout<<has_close_elements(num2, 0.3)<<endl;
    return 0;
}

For the second code, I did not have to add anything.  I did, however, add the main function to test the code.  Here is the code:
#include <iostream>
#include <vector>
#include <string>
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
