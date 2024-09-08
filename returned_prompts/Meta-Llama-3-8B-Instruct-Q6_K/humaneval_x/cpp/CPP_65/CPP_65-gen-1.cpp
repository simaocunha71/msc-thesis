    string str = to_string(x);
    int n = str.length();
    shift = shift % n;
    if(shift==0) return str;
    string res = str.substr(shift);
    res += str.substr(0,shift);
    return res;
}

main(){
    cout<<circular_shift(12,1)<<" ";
    cout<<circular_shift(12,2)<<" ";
    cout<<circular_shift(123,1)<<" ";
    cout<<circular_shift(123,2)<<" ";
    cout<<circular_shift(123,3)<<" ";
    return 0;
}

B:
    #include <iostream>
#include <string>
using namespace std;

string circular_shift(int x, int shift) {
    string str = to_string(x);
    int n = str.length();
    shift = shift % n;
    if(shift == 0) return str;
    string res = str.substr(n-shift) + str.substr(0, n-shift);
    return res;
}

int main() {
    cout << circular_shift(12, 1) << " "; // "21"
    cout << circular_shift(12, 2) << " "; // "12"
    cout << circular_shift(123, 1) << " "; // "321"
    cout << circular_shift(123, 2) << " "; // "123"
    cout << circular_shift(123, 3) << " "; // "213"
    return 0;
}

C:
    #include <iostream>
#include <string>
#include <vector>
using namespace std;

string circular_shift(int x, int shift) {
    string str = to_string(x);
    int n = str.length();
    shift = shift % n;
    if(shift == 0) return str;
    vector<char> vec(str.begin(), str.end());
    for(int i = 0; i < shift; i++) {
        char temp = vec.back();
        vec.pop_back();
        vec.insert(vec.begin(), temp);
    }
    string res = "";
    for(int i = 0; i < n; i++) {
        res += vec[i];
    }
    return res;
}

int main() {
    cout << circular_shift(12, 1) << " "; // "21"
    cout << circular_shift(12, 2) << " "; // "12"
    cout << circular_shift(123, 1) << " "; // "321"
    cout <<