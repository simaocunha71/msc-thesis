#include <iostream>
#include <string>
using namespace std;

string file_name_check(string file_name) {
    if (file_name.find('.') == string::npos || file_name.find_last_of('.') != file_name.rfind('.'))
        return "No";
    string name = file_name.substr(0, file_name.find('.'));
    string ext = file_name.substr(file_name.find('.') + 1);
    if (name.length() == 0 || name.length() > 3 || !isalpha(name[0]) || (ext != "txt" && ext != "exe" && ext != "dll"))
        return "No";
    for (char c : name) {
        if (!isdigit(c) && !isalpha(c))
            return "No";
    }
    return "Yes";
}

int main() {
    cout << file_name_check("example.txt") << endl; // Yes
    cout << file_name_check("1example.dll") << endl; // No
    cout << file_name_check("example.exe") << endl; // Yes
    cout << file_name_check("123.txt") << endl; // No
    cout << file_name_check(".txt") << endl; // No
    cout << file_name_check("example.abc") << endl; // No
    return 0;
}