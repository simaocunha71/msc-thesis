#include <set>
#include <string>
#include <algorithm>

int count_distinct_characters(string str) {
    set<char> distinct_chars;
    for (char c : str) {
        distinct_chars.insert(tolower(c));
    }
    return distinct_chars.size();
}

int main() {
    string s = "Jerry";
    int distinct_count = count_distinct_characters(s);
    printf("%d\n", distinct_count); // 输出 4
    return 0;
}

