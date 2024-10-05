    vector<int> res(2,0);
    for(int i=1;i<=n;i++){
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if(s==r){
            if(i%2==0)
                res[0]++;
            else
                res[1]++;
        }
    }
    return res;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)\n", res[0], res[1]);
    return 0;
}

*/

// C++ solution for the above problem
#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool isPalindrome(int n) {
    string s = to_string(n);
    string r = s;
    reverse(r.begin(), r.end());
    return s == r;
}

vector<int> even_odd_palindrome(int n) {
    vector<int> res(2, 0);
    for (int i = 1; i <= n; i++) {
        if (isPalindrome(i)) {
            if (i % 2 == 0)
                res[0]++;
            else
                res[1]++;
        }
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    vector<int> res = even_odd_palindrome(n);
    cout << "(" << res[0] << ", " << res[1] << ")\n";
    return 0;
}

// C++ solution for the above problem
#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool isPalindrome(int n) {
    string s = to_string(n);
    string r = s;
    reverse(r.begin(), r.end());
