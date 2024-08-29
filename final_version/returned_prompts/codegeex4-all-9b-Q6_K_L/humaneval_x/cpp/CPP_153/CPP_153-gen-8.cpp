#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Extension {
public:
    string name;
    int strength;

    Extension(string n, int s) : name(n), strength(s) {}
};

bool compare(Extension a, Extension b) {
    return a.strength < b.strength;
}

string strongest_extension(string class_name, vector<string> extensions) {
    vector<Extension> exts;

    for (int i = 0; i < extensions.size(); i++) {
        string name = extensions[i];
        int strength = 0;

        for (int j = 0; j < name.size(); j++) {
            if (isupper(name[j])) {
                strength++;
            } else if (islower(name[j])) {
                strength--;
            }
        }

        exts.push_back(Extension(name, strength));
    }

    sort(exts.begin(), exts.end(), compare);

    return class_name + "." + exts[0].name;
}

int main() {
    vector<string> extensions = {"AA", "Be", "CC"};
    string class_name = "my_class";
    cout << strongest_extension(class_name, extensions) << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Extension {
public:
    string name;
    int strength;

    Extension(string n, int s) : name(n), strength(s) {}
};

bool compare(Extension a, Extension b) {
    return a.strength < b.strength;
}

string strongest_extension(string class_name, vector<string> extensions) {
    vector<Extension> exts;

    for (int i = 0; i < extensions.size(); i++) {
        string name = extensions[i];
        int strength = 0;

        for (int j = 0; j < name.size(); j++) {
            if (isupper(name[j])) {
                strength++;
            } else if (islower(name[j])) {
                strength--;
            }
        }

        exts.push_back(Extension(name, strength));
    }

    sort(exts.begin(), exts.end(), compare);

    return class_name + "." + exts[0].name;
}

int main() {
    vector<string> extensions = {"AA", "Be", "CC"};
    string class_name = "my_class";
    cout << strongest_extension(class_name, extensions) << endl;
    return 0;
}

B:
#include <