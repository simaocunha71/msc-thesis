    vector<string> result;
    string temp;
    for(int i=0; i<s.length(); i++) {
        if(s[i] == ',' || s[i] == ' ') {
            if(!temp.empty()) {
                result.push_back(temp);
                temp.clear();
            }
        } else {
            temp += s[i];
        }
    }
    if(!temp.empty()) {
        result.push_back(temp);
    }
    return result;
}

int main() {
    string s = "Hi, my name is John";
    vector<string> result = words_string(s);
    for(int i=0; i<result.size(); i++) {
        printf("%s\n", result[i].c_str());
    }
    return 0;
}

