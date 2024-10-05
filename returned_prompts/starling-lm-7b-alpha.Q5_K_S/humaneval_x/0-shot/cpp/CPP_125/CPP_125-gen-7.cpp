    int len = txt.size();
    int cnt = 0;
    int index = 0;
    vector<string> vec;
    for(int i = 0; i < len; i++) {
        if(txt[i] != ' ' && txt[i] != ',' && txt[i] != '.') {
            cnt++;
        } else if(txt[i] == ' ' || txt[i] == ',' || txt[i] == '.') {
            vec.push_back(txt.substr(index,cnt));
            cnt = 0;
            index = i+1;
        }
    }
    if(cnt != 0) {
        vec.push_back(txt.substr(index,cnt));
    }
    return vec;
}

vector<string> split_words(char *txt) {
    string str = "";
    for(int i = 0; i < strlen(txt); i++) {
        str += txt[i];
        if(txt[i] == ' ' || txt[i] == ',' || txt[i] == '.') {
            vec.push_back(str);
            str = "";
        }
    }
    if(str != "") {
        vec.push_back(str);
    }
    return vec;
}

int main() {
    string txt = "Hello world!";
    vector<string> res = split_words(txt);
    for(int i = 0; i < res.size(); i++) {
        printf("%s\n",res[i].c_str());
    }
    return 0;
}





*/























































































































