    vector<int> result(2,0);
    for(int i=1; i<=n; i++){
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if(s == r){
            if(i % 2 == 0)
                result[0]++;
            else
                result[1]++;
        }
    }
    return result;
}
int main(){
    int n;
    scanf("%d", &n);
    vector<int> ans = even_odd_palindrome(n);
    printf("(%d, %d)\n", ans[0], ans[1]);
    return 0;
}

*/

//Solving the problem by using the above C++ code

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){
    vector<int> result(2,0);
    for(int i=1; i<=n; i++){
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if(s == r){
            if(i % 2 == 0)
                result[0]++;
            else
                result[1]++;
        }
    }
    return result;
}
int main(){
    int n;
    scanf("%d", &n);
    vector<int> ans = even_odd_palindrome(n);
    printf("(%d, %d)\n", ans[0], ans[1]);
    return 0;
}

//Solved by using C++ language. C++ language has built-in libraries to perform string and vector manipulation. Firstly, we are converting the given integer to string and then reversing it to check whether it is a palindrome or not. If it is a palindrome, then we are checking whether it is even or odd and incrementing the count accordingly.

//Time complexity for the given code is O(n^2