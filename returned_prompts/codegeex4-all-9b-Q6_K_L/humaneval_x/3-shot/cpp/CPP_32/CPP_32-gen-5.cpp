
You need to #include <algorithm> to use std::abs in your has_close_elements function.  Also, you need to provide the definition of the round function in your truncate_number function.  You can use the <cmath> header for this purpose.  Here is the corrected code:

#include<stdio.h>
#include<cmath>
#include<vector>
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
#include<cmath>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        }
        if (chr==')'){
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
#include<math.h>
#include<vector>
using namespace std;
double poly(vector<double> xs, double x){
    double sum=0;
    int i;
    for (i=0;i<xs.size();i++){
        sum+=xs[i]*pow(x,i);
    }
    return sum;
}

double find_zero(vector<double> xs){
    double a,b,c,x1,x2;
    a=xs[0];
    b