    vector<string> res;
    string temp = "";
    for(int i = 0; i < txt.length(); i++) {
        if(txt[i] == ' ' || txt[i] == ',') {
            if(temp != "") {
                res.push_back(temp);
                temp = "";
            }
        }
        else {
            temp += txt[i];
        }
    }
    if(temp != "") {
        res.push_back(temp);
    }
    else {
        int count = 0;
        for(int i = 0; i < 26; i++) {
            if((txt[0] - 'a' + i) % 2 != 0) {
                count++;
            }
        }
        res.push_back(to_string(count));
    }
    return res;
}

int main() {
    string txt = "Hello,world!";
    vector<string> res = split_words(txt);
    for(int i = 0; i < res.size(); i++) {
        printf("%s\n", res[i].c_str());
    }
    return 0;
}

Output:
Hello
world!