    int i=0,cnt=0;
    while(i<S.length()){
        if(S[i]=='I'){
            while(S[i]!=','&&S[i]!='.'&&S[i]!='!'&&S[i]!=';'&&S[i]!='?'){
                i++;
            }
            cnt++;
        }
        i++;
    }
    return cnt;
}
int main()
{
    string s;
    cin>>s;
    cout<<is_bored(s);
    return 0;
}

*/

/*
You need to write a program that will calculate the sum of all the even numbers in a given string.

For example:
>>> sum_of_evens("1234567")
18
>>> sum_of_evens("1234567890")
0
>>> sum_of_evens("abcdefghijklmnopqrstuvwxyz")
0
*/
#include<stdio.h>
#include<string>
using namespace std;
int sum_of_evens(string S){

    int i=0,sum=0,len=S.length();
    while(i<len){
        if(S[i]%2==0){
            sum+=S[i];
        }
        i++;
    }
    return sum;
}
int main(){
    string s;
    cin>>s;
    cout<<sum_of_evens(s);
    return 0;
}


/*
You will be given a string of words and your job is to remove all the vowels from the string.

For example:
>>> remove_vowels("Hello world")
"hll wrld"
>>> remove_vowels("The sky is blue. The sun is shining. I love this weather")
"Th sk s bl. Th s shng. I lv ths wthr"
*/
#include<stdio.h>
#include<string>
using namespace std;
string remove_vowels(string S){
    string res="";