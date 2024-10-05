    if(strings.size() == 0) return "";
    int max_len = 0;
    string longest_string = "";
    for(string s : strings){
        if(s.length() > max_len){
            max_len = s.length();
            longest_string = s;
        }
    }
    return longest_string;

}

int main(){
    vector<string> strings;
    strings.push_back("a");
    strings.push_back("bb");
    strings.push_back("ccc");
    strings.push_back("d");
    strings.push_back("ee");
    string longest = longest(strings);
    printf("%s\n", longest.c_str());
}
