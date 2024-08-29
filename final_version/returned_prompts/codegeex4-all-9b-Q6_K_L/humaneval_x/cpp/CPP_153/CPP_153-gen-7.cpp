#include <algorithm>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    int max_strength = -1000;
    string result = "";

    for (string extension : extensions) {
        int strength = 0;
        for (char c : extension) {
            if (isupper(c))
                strength++;
            else if (islower(c))
                strength--;
        }

        if (strength > max_strength) {
            max_strength = strength;
            result = extension;
        }
    }

    return class_name + "." + result;
}
