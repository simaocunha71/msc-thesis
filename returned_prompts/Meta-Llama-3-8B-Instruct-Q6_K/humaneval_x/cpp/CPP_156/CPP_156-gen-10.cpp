    vector< pair<int, string> > roman_map = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};
    string result = "";
    for(int i = 0; i < roman_map.size(); i++){
        while(number >= roman_map[i].first){
            number -= roman_map[i].first;
            result += roman_map[i].second;
        }
    }
    return result;
}
int main(){
    printf("%s\n", int_to_mini_romank(19).c_str());
    printf("%s\n", int_to_mini_romank(152).c_str());
    printf("%s\n", int_to_mini_romank(426).c_str());
    return 0;
}

