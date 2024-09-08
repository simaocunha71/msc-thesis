#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int count1 = 0;
    int count2 = 0;

    for (int i = 0; i < lst1.size(); i++) {
        count1 += lst1[i].length();
    }

    for (int i = 0; i < lst2.size(); i++) {
        count2 += lst2[i].length();
    }

    if (count1 < count2) {
        return lst1;
    } else if (count2 < count1) {
        return lst2;
    } else {
        return lst1;
    }
}

int main() {
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};

    vector<string> result = total_match(lst1, lst2);

    for (int i = 0; i < result.size(); i++) {
        printf("%s\n", result[i].c_str());
    }

    return 0;
}
