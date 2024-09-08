    vector<int> res;
    int i;
    int even=0, odd=0;

    for(i=1; i<=n; i++){
        string s = to_string(i);
        string rev = s;
        reverse(rev.begin(), rev.end());

        if(s==rev){
            if(i%2==0){
                even++;
            }else{
                odd++;
            }
        }
    }

    res.push_back(even);
    res.push_back(odd);

    return res;

}
int main(){
    vector<int> res = even_odd_palindrome(12);
    for(int i=0; i<res.size(); i++){
        printf("%d\n", res[i]);
    }
    return 0;
}
B:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){

    vector<int> res;
    int i;
    int even=0, odd=0;

    for(i=1; i<=n; i++){
        string s = to_string(i);
        string rev = s;
        reverse(rev.begin(), rev.end());

        if(s==rev){
            if(i%2==0){
                even++;
            }else{
                odd++;
            }
        }
    }

    res.push_back(even);
    res.push_back(odd);

    return res;

}
int main(){
    vector<int> res = even_odd_palindrome(12);
    for(int i=0; i<res.size(); i++){
        printf("%d\n", res[i]);
    }
    return 0;
}
C:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){

    vector<int> res;
    int i;
    int even=0, odd=0;

    for(i=1; i<=n; i++){
        string s = to_string(i);
        string rev = s;
        reverse(rev.begin(), rev.end());

        if(s==rev){
            if(i%2==0){
                even++;
            }else{
                odd++;
            }
        }
    }

    res.push_back(even);
    res.push_back(odd);

    return res;

}
int main(){
    vector<int> res = even_odd_palindrome(12);
    for(int i=0; i<res.size(); i++){
        printf("%d\n", res[i]);
    }
    return 0;
}
D:
#include<stdio.h>
#include