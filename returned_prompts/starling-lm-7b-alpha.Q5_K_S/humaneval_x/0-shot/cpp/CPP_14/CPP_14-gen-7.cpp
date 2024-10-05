    vector<string> res;
    res.push_back(str);
    for(int i = 0; i < str.length(); i++) {
        str = str.substr(0, i + 1);
        res.push_back(str);
    }
    return res;
}


// Test Cases
void test_case_1(){
    vector<string> res = all_prefixes("abc");
    string expected[] = {"a", "ab", "abc"};
    for(int i = 0; i < res.size(); i++) {
        if(res[i] != expected[i]) {
            printf("Test Case 1 Failed\n");
            return;
        }
    }
    printf("Test Case 1 Passed\n");
}

void test_case_2(){
    vector<string> res = all_prefixes("abcdef");
    string expected[] = {"a", "ab", "abc", "abcd", "abcde", "abcdef"};
    for(int i = 0; i < res.size(); i++) {
        if(res[i] != expected[i]) {
            printf("Test Case 2 Failed\n");
            return;
        }
    }
    printf("Test Case 2 Passed\n");
}

void test_case_3(){
    vector<string> res = all_prefixes("");
    string expected[] = {};
    for(int i = 0; i < res.size(); i++) {
        if(res[i] != expected[i]) {
            printf("Test Case 3 Failed\n");
            return;
        }
    }
    printf("Test Case 3 Passed\n");
}

void test_case_4(){
    vector<string> res = all_prefixes("ab");
    string expected[] = {"a", "ab"};
    for(int i = 0; i < res.size(); i++) {
        if(res[i] != expected[i]) {
            printf("Test Case 4 Failed\n");
            return;
        }
    }
    printf("Test Case 