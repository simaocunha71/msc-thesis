    map<char, int> result;
    int maxCount = 0;
    for (char c : test) {
        if (c == ' ') {
            continue;
        }
        if (result.find(c) == result.end()) {
            result[c] = 1;
        } else {
            result[c]++;
        }
        if (result[c] > maxCount) {
            maxCount = result[c];
        }
    }
    map<char, int> maxResult;
    for (auto& it : result) {
        if (it.second == maxCount) {
            maxResult[it.first] = it.second;
        }
    }
    return maxResult;
}

int main() {
    printf("%s\n", histogram("a b c").toString().c_str());
    printf("%s\n", histogram("a b b a").toString().c_str());
    printf("%s\n", histogram("a b c a b").toString().c_str());
    printf("%s\n", histogram("b b b b a").toString().c_str());
    printf("%s\n", histogram("").toString().c_str());
    return 0;
}

B:
    #include <iostream>
    #include <map>
    #include <string>
    using namespace std;

    map<pair<char, int>, int> histogram(string test) {
        map<char, int> result;
        map<pair<char, int>, int> maxResult;
        int maxCount = 0;
        for (char c : test) {
            if (c == ' ') {
                continue;
            }
            if (result.find(c) == result.end()) {
                result[c] = 1;
            } else {
                result[c]++;
            }
            if (result[c] > maxCount) {
                maxCount = result[c];
                maxResult.clear();
                maxResult[make_pair(c, result[c])] = 1;
            } else if (result[c] == maxCount) {
                maxResult[make_pair(c, result[c])] = 1;
            }
        }
        return maxResult;
    }

    int main() {
        for (auto& it : histogram("a b c")) {
            cout << "(" << it.first.first << ", " << it.first.second << ")" << endl;
        }
        for (auto& it : histogram("a b b a")) {
            cout << "(" << it.first.first << ", " << it.first.second << ")" << endl;
        }
        for (