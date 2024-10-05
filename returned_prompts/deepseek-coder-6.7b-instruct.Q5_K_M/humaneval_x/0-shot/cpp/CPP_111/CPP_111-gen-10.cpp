    map<char,int> letter_map;
    int max_count = 0;
    map<char,int> result;

    for(char c : test){
        if(c == ' ') continue;
        letter_map[c]++;
        if(letter_map[c] > max_count) max_count = letter_map[c];
    }

    for(auto pair : letter_map){
        if(pair.second == max_count) result.insert(pair);
    }
    return result;
}

int main(){
    map<char,int> res = histogram("b b b b a");
    for(auto pair : res)
        printf("{%c, %d}, ", pair.first, pair.second);
    return 0;
}

*/

