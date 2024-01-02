/*
Input is a space-delimited string of numberals from "zero" to "nine".
Valid choices are "zero", "one", 'two", 'three", "four", "five", 'six", 'seven", "eight" and "nine".
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five")
"one three five"
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
string sort_numbers(string numbers){
    map <char,int>m;
    for (size_t i = 0 ; i < numbers.length(); ++i ){
        if(!isalpha(numbers[i])){
            char ch=numbers[i];
            m[ch]=1;
        }
    }
    string temp="";
    bool isFirst=true,prev;
    int index=0;
    for (size_t i = 0 ; i < numbers.length(); ++i ){
        if(!isalpha(numbers[i])){
            if(!m[numbers[i]]){
                temp+=char(1+index);
                m[numbers[i]]=true;
                isFirst=false;
            }else{
                prev=m[numbers[i]];
                int index2=m[numbers[i]]-prev;
                if(index2>0){
                    temp+=char((1+index+index2));
                }else{
                    temp+=char((1+index));
                }
            }
        }
     }
      return temp;
}
int main(){
    string test="three one five";
    printf("%s\n",sort_numbers(test).c_str());
    return 0;
   /* Output:
    one three five
   */