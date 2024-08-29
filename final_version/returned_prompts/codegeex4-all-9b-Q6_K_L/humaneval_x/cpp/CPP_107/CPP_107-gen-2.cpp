#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){
    int even=0,odd=0;
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        string r(s.rbegin(),s.rend());
        if(s==r){
            if(i%2==0)
                even++;
            else
                odd++;
        }
    }
    return {even,odd};
}

