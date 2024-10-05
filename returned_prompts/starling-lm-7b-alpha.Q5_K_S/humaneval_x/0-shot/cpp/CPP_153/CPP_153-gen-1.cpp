
#include <bits/stdc++.h>
using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions) {
    string ans;
    int max = -1;
    for (auto x : extensions) {
        int cap = 0, sm = 0;
        for (char c : x) {
            if ('A' <= c && c <= 'Z') cap++;
            else if ('a' <= c && c <= 'z') sm++;
        }
        if (cap - sm > max) {
            max = cap - sm;
            ans = class_name + "." + x;
        }
    }
    return ans;
}

int main() {
    vector<string> extensions = {"SErviNGSliCes", "Cheese", "StuFfed"};
    string class_name = "Slices";
    cout << Strongest_Extension(class_name, extensions) << endl;
    return 0;
}


































































