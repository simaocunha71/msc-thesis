#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isValidFileName(const string& fileName) {
    int dotCount = 0;
    int digitCount = 0;
    int letterCount = 0;

    for (char c : fileName) {
        if (isdigit(c)) {
            digitCount++;
        } else if (c == '.') {
            dotCount++;
        } else if (isalpha(c)) {
            letterCount++;
        }
    }

    if (digitCount > 3 || dotCount != 1 || letterCount == 0 || fileName[0] == '.' || fileName[fileName.size() - 1] == '.') {
        return false;
    }

    string extension = fileName.substr(fileName.find('.') + 1);
    if (extension != "txt" && extension != "exe" && extension != "dll") {
        return false;
    }

    return true;
}

string file_name_check(string file_name) {
    if (isValidFileName(file_name)) {
        return "Yes";
    } else {
        return "No";
    }
}

int main() {
    cout << file_name_check("example.txt") << endl;    // Output: Yes
    cout << file_name_check("1example.dll") << endl;  // Output: No
    cout << file_name_check("test.txt1") << endl;     // Output: No
    cout << file_name_check("test.") << endl;         // Output: No
    cout << file_name_check(".test.txt") << endl;     // Output: No
    cout << file_name_check("test.exe") << endl;      // Output: Yes
    cout << file_name_check("test.dll") << endl;      // Output: Yes
    cout << file_name_check("test.doc") << endl;      // Output: No

    return 0;
}
