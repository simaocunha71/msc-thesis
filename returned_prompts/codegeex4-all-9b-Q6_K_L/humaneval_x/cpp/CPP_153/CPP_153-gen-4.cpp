#include <iostream>
#include <vector>
#include <string>
using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    int max_strength = -10000;
    string strongest_extension;

    for (int i = 0; i < extensions.size(); i++) {
        int strength = 0;
        string extension = extensions[i];

        for (char c : extension) {
            if (isupper(c)) {
                strength++;
            } else if (islower(c)) {
                strength--;
            }
        }

        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }

    return class_name + "." + strongest_extension;
}

int main() {
    string class_name = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    string result = Strongest_Extension(class_name, extensions);
    cout << result << endl;  // Output: my_class.AA

    return 0;
}
