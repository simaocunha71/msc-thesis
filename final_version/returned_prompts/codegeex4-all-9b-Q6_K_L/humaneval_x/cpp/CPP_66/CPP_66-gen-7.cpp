#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

int main() {
    string s = "abAB";
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += int(c);
        }
    }
    cout << sum << endl;
    return 0;
}

C:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += c;
        }
    }
    return sum;
}

int main() {
    string s = "abAB";
    cout << digitSum(s) << endl;
    return 0;
}

D:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += c;
        }
    }
    return sum;
}

int main() {
    string s = "abAB";
    cout << digitSum(s) << endl;
    return 0;
}

E:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += c;
        }
    }
    return sum;
}

int main() {
    string s = "abAB";
    cout << digitSum(s) << endl;
    return 0;
}

F:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += c;
        }
    }
    return sum;
}

int main() {
    string s = "abAB";
    cout << digitSum(s) << endl;
    return 0;
}

G:
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += c;
        }
    }
    return sum;
}

