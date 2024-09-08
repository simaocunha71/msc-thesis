

C:
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string Strongest_Extension(string className, vector<string> extensions) {
    string strongestExtension = "";
    int maxStrength = -1000000;

    for (string extension : extensions) {
        int cap = 0, sm = 0;

        for (char c : extension) {
            if (isupper(c)) {
                cap++;
            } else {
                sm++;
            }
        }

        int strength = cap - sm;

        if (strength > maxStrength) {
            maxStrength = strength;
            strongestExtension = extension;
        }
    }

    return className + "." + strongestExtension;
}

int main() {
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};

    cout << Strongest_Extension(className, extensions) << endl;

    return 0;
}
