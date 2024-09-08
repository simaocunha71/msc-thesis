#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool compare(string s1, string s2) {
    if (s1.length() == s2.length())
        return s1 < s2;
    return s1.length() < s2.length();
}

vector<string> vector_sort(vector<string> lst) {
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i].length() % 2 == 1)
            lst.erase(lst.begin() + i);
    }
    sort(lst.begin(), lst.end(), compare);
    return lst;
}

int main() {
    vector<string> v1 = {"aa", "a", "aaa"};
    vector<string> v2 = {"ab", "a", "aaa", "cd"};

    vector<string> result1 = vector_sort(v1);
    vector<string> result2 = vector_sort(v2);

    for (int i = 0; i < result1.size(); i++)
        cout << result1[i] << " ";
    cout << endl;

    for (int i = 0; i < result2.size(); i++)
        cout << result2[i] << " ";
    cout << endl;

    return 0;
}
B:
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool compare(string s1, string s2) {
    if (s1.length() == s2.length())
        return s1 < s2;
    return s1.length() < s2.length();
}

vector<string> vector_sort(vector<string> lst) {
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i].length() % 2 == 1)
            lst.erase(lst.begin() + i);
    }
    sort(lst.begin(), lst.end(), compare);
    return lst;
}

int main() {
    vector<string> v1 = {"aa", "a", "aaa"};
    vector<string> v2 = {"ab", "a", "aaa", "cd"};

    vector<string> result1 = vector_sort(v1);
    vector<string> result2 = vector_sort(v2);

    for (int i = 0; i < result1.size(); i++)
        printf("%s ", result1[i].c_str());
    printf("\n");

    for (int i =