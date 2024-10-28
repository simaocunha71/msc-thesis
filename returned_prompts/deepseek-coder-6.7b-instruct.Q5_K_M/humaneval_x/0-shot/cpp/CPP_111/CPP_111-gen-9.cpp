    map<char,int> result;
    int max_count = 0;
    for(char c : test){
        if(c == ' ') continue;
        result[c]++;
        if(result[c] > max_count) max_count = result[c];
    }
    map<char,int> final_result;
    for(auto i : result){
        if(i.second == max_count) final_result[i.first] = i.second;
    }
    return final_result;
}

// You can test the function with the following main function

int main() {

    auto result = histogram("a b c");
    for(auto i : result)
        printf("%c : %d\n", i.first, i.second);

    result = histogram("a b b a");
    for(auto i : result)
        printf("%c : %d\n", i.first, i.second);

    result = histogram("a b c a b");
    for(auto i : result)
        printf("%c : %d\n", i.first, i.second);

    result = histogram("b b b b a");
    for(auto i : result)
        printf("%c : %d\n", i.first, i.second);

    result = histogram("");
    for(auto i : result)
        printf("%c : %d\n", i.first, i.second);

    return 0;
}

*/

