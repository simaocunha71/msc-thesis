#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    int max_strength = -1000;
    string max_extension = "";
    for(auto extension : extensions) {
        int strength = 0;
        for(auto c : extension)
            if(isupper(c)) strength++;
            else if(islower(c)) strength--;
        if(strength > max_strength) {
            max_strength = strength;
            max_extension = extension;
        }
    }
    return class_name + '.' + max_extension;
}
C:
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    int max_strength = -1000;
    string max_extension = "";
    for(auto extension : extensions) {
        int strength = 0;
        for(auto c : extension)
            if(isupper(c)) strength++;
            else if(islower(c)) strength--;
        if(strength > max_strength) {
            max_strength = strength;
            max_extension = extension;
        }
    }
    return class_name + '.' + max_extension;
}

