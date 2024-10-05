    int sum = 0;
    for (int i = 0; i < s.length(); i++){
        if (isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}

int main(){
    string s;
    cout << "Enter a string: ";
    cin >> s;
    cout << digitSum(s) << endl;
    return 0;
}


A: 
The problem is that you are trying to use the isupper() function, but this function is from the cctype library, not from the standard string library. 

Solution:

Include the cctype library at the beginning of your program. 

#include <cctype>

Also, make sure to use the std namespace:

using namespace std;

So, your corrected code would be:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        if (isupper(s[i])) {
            sum += int(s[i]);
        }
    }
    return sum;
}

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;
    cout << digitSum(s) << endl;
    return 0;
}

This code will correctly determine the sum of the ASCII values of uppercase characters in a string.


