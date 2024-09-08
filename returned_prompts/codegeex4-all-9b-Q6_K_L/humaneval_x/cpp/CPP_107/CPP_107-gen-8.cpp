#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> even_odd_palindrome(int n) {
    int even = 0;
    int odd = 0;
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        string revStr = str;
        reverse(revStr.begin(), revStr.end());
        if(str == revStr) {
            if(i % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
    }
    return {even, odd};
}

int main() {
    int n;
    cin >> n;
    vector<int> result = even_odd_palindrome(n);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> even_odd_palindrome(int n) {
    int even = 0;
    int odd = 0;
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        string revStr = str;
        reverse(revStr.begin(), revStr.end());
        if(str == revStr) {
            if(i % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
    }
    return {even, odd};
}

int main() {
    int n;
    cin >> n;
    vector<int> result = even_odd_palindrome(n);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
C:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> even_odd_palindrome(int n) {
    int even = 0;
    int odd = 0;
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        string revStr = str;
        reverse(revStr.begin(), revStr.end());
        if(str == revStr) {
            if(i % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
    }
    return {even, odd};
}

int main() {
    int n;
    cin >> n;
    vector<int> result = even_odd_palindrome(n);
    cout << result[0] << " "