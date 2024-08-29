#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string Strength(const string& ext) {
    int upper = 0, lower = 0;
    for (auto c : ext) {
        if (isupper(c)) ++upper;
        else if (islower(c)) ++lower;
    }
    return to_string(upper - lower);
}

string Strongest_Extension(const string& class_name, vector<string> extensions) {
    string res = class_name;
    if (extensions.empty()) return res;

    string ext = extensions[0];
    string max_strength = Strength(ext);
    for (auto& e : extensions) {
        string strength = Strength(e);
        if (strength > max_strength) {
            max_strength = strength;
            ext = e;
        }
    }
    return res + '.' + ext;
}

C:
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string Strength(const string& ext) {
    int upper = 0, lower = 0;
    for (auto c : ext) {
        if (isupper(c)) ++upper;
        else if (islower(c)) ++lower;
    }
    return to_string(upper - lower);
}

string Strongest_Extension(const string& class_name, vector<string> extensions) {
    if (extensions.empty()) return class_name;
    string max_ext = extensions[0];
    string max_strength = Strength(max_ext);
    for (auto& ext : extensions) {
        string strength = Strength(ext);
        if (strength > max_strength) {
            max_strength = strength;
            max_ext = ext;
        }
    }
    return class_name + '.' + max_ext;
}

D:
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string Strength(const string& ext) {
    int upper = 0, lower = 0;
    for (auto c : ext) {
        if (isupper(c)) ++upper;
        else if (islower(c)) ++lower;
    }
    return to_string(upper - lower);
}

string Strongest_Extension(const string& class_name, vector<string> extensions) {
    if (extensions.empty()) return class_name;
    string max_ext = extensions[0];
    string max_strength = Strength(max_ext);
    for (int i = 1; i < extensions.size(); ++i) {
        string strength = Strength(extensions[i]);
        if (strength >