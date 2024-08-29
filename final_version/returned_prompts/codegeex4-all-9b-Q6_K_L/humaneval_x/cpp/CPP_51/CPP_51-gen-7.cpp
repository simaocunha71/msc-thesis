#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string input;
    getline(cin, input);
    string vowels = "aeiouAEIOU";
    input.erase(remove(input.begin(), input.end(), 'a'), input.end());
    input.erase(remove(input.begin(), input.end(), 'e'), input.end());
    input.erase(remove(input.begin(), input.end(), 'i'), input.end());
    input.erase(remove(input.begin(), input.end(), 'o'), input.end());
    input.erase(remove(input.begin(), input.end(), 'u'), input.end());
    cout << input << endl;
    return 0;
}
B:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string input;
    getline(cin, input);
    string vowels = "aeiouAEIOU";
    for(int i = 0; i < input.size(); i++) {
        if(vowels.find(input[i]) != string::npos) {
            input.erase(i, 1);
            i--;
        }
    }
    cout << input << endl;
    return 0;
}
C:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string input;
    getline(cin, input);
    string vowels = "aeiouAEIOU";
    for(int i = 0; i < input.size(); i++) {
        if(vowels.find(input[i]) != string::npos) {
            input.erase(input.begin() + i);
            i--;
        }
    }
    cout << input << endl;
    return 0;
}
D:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string input;
    getline(cin, input);
    string vowels = "aeiouAEIOU";
    for(int i = 0; i < input.size(); i++) {
        if(vowels.find(input[i]) != string::npos) {
            input.erase(input.begin() + i);
        }
    }
    cout << input << endl;
    return 0;
}
E:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string input;
    getline(cin, input);
    string vowels = "aeiouAEIOU";
    for(int i = 0; i < input.size(); i++) {
        if(vowels.find(input[i]) != string::npos)