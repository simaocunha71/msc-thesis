    vector<string> res;
    string temp = "";
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == ',' || s[i] == ' ')
            if(!temp.empty()) {
                res.push_back(temp);
                temp = "";
            }
        else
            temp += s[i];
    }
    if(!temp.empty())
        res.push_back(temp);

    return res;
}

int main() {
    vector<string> result = words_string("Hi, my name is John");
    for(int i = 0; i < result.size(); i++) {
        printf("%s\n", result[i].c_str());
    }
    return 0;
}

