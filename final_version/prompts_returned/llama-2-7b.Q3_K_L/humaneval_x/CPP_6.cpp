/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    int depth=0;
    vector<int> retVal;//initialized with 1
    int i,j;//iterating the string

    for (i = 0; i < paren_string.length(); i++) {
        if(paren_string[i] == '('){
            depth++; //if a parenthesis is encountered then increment the depth by one
            retVal[depth]++;
            j=i+1;//iterating the string so as to include the next character too
            while(j<paren_string.length() && paren_string[j]!=')' ) { //while the next character is not a ')' then add 1 to the depth and increment j by one
                retVal[depth+1]++;//incrementing the depth after each occurence of '('
                j++;
            }
        }else{
             if(paren_string[i] == ')'){ //if a ')' is encountered then decrease the depth and reset it to 0
                 if(depth ==0)return retVal;//the returned value is initialized with only 1, now decreasing and resetting it to zero will return nothing
                for (j = depth - 2 ; j >=0; j--) {
                    retVal[j]--; //decrease by one the values for each level of nesting that has been visited by the ')'
                }
            }
        }
    }
}
int main(){
    string paren_string = "(()()) ((())) () ((())()());";//input to this function is taken from standard input as a string.
    cout<<"