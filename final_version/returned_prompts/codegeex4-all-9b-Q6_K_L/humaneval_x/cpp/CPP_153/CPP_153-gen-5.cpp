#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    string maxStr = "";
    int max = 0;
    for (auto s : extensions) {
        int count = 0;
        for (auto c : s) {
            if (c >= 'A' && c <= 'Z')
                count++;
        }
        if (count > max) {
            max = count;
            maxStr = s;
        }
    }
    return class_name + "." + maxStr;
}

int main() {
    // Example usage
    vector<string> extensions = {"AA", "Be", "CC"};
    string result = Strongest_Extension("my_class", extensions);
    printf("%s\n", result.c_str());  // Output: my_class.AA

    return 0;
}