#include <iostream>
#include <string>
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
    cout << digitSum("") << endl; // 0
    cout << digitSum("abAB") << endl; // 131
    cout << digitSum("abcCd") << endl; // 67
    cout << digitSum("helloE") << endl; // 69
    cout << digitSum("woArBld") << endl; // 131
    cout << digitSum("aAaaaXa") << endl; // 153
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += (int)c;
        }
    }
    return sum;
}

int main() {
    cout << digitSum("") << endl; // 0
    cout << digitSum("abAB") << endl; // 131
    cout << digitSum("abcCd") << endl; // 67
    cout << digitSum("helloE") << endl; // 69
    cout << digitSum("woArBld") << endl; // 131
    cout << digitSum("aAaaaXa") << endl; // 153
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

int digitSum(string s) {
    int sum = 0;
    for (char c : s) {
        if (isupper(c)) {
            sum += (int) c;
        }
    }
    return sum;
}

int main() {
    cout << digitSum("") << endl; // 0
    cout << digitSum("abAB") << endl; // 131
    cout << digitSum("abcCd") << endl; // 67
    cout << digitSum("helloE") << endl; // 69
    cout << digitSum("woArBld") << endl; // 131
    cout << digitSum("aAaaaXa") << endl; // 153
    return 0;
}

D:
#include <iostream>
#include <