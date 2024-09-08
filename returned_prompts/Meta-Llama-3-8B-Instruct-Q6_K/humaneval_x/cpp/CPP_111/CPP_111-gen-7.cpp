    map<char,int> result;
    int max_count = 0;
    for (int i = 0; i < test.length(); i++) {
        char ch = test[i];
        if (result.find(ch) != result.end()) {
            result[ch]++;
        } else {
            result[ch] = 1;
        }
        if (result[ch] > max_count) {
            max_count = result[ch];
        }
    }
    map<char, int> max_result;
    for (auto it = result.begin(); it != result.end(); it++) {
        if (it->second == max_count) {
            max_result[it->first] = it->second;
        }
    }
    return max_result;
}

int main() {
    string test1 = "a b c";
    string test2 = "a b b a";
    string test3 = "a b c a b";
    string test4 = "b b b b a";
    string test5 = "";

    map<char,int> result1 = histogram(test1);
    map<char,int> result2 = histogram(test2);
    map<char,int> result3 = histogram(test3);
    map<char,int> result4 = histogram(test4);
    map<char,int> result5 = histogram(test5);

    for(auto it = result1.begin(); it != result1.end(); it++){
        printf("(%c, %d)\n", it->first, it->second);
    }
    for(auto it = result2.begin(); it != result2.end(); it++){
        printf("(%c, %d)\n", it->first, it->second);
    }
    for(auto it = result3.begin(); it != result3.end(); it++){
        printf("(%c, %d)\n", it->first, it->second);
    }
    for(auto it = result4.begin(); it != result4.end(); it++){
        printf("(%c, %d)\n", it->first, it->second);
    }
    for(auto it = result5.begin(); it != result5.end(); it++){
        printf("(%c, %d)\n", it->first, it->second);
    }

    return 0;
}
