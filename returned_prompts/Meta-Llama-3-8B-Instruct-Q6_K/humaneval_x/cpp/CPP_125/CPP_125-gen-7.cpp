    vector<string> res;
    for(int i = 0; i < txt.size(); i++){
        if(txt[i] == ' '){
            string temp = txt.substr(0, i);
            res.push_back(temp);
            txt = txt.substr(i + 1);
            i = -1;
        }
        else if(txt[i] == ','){
            string temp = txt.substr(0, i);
            res.push_back(temp);
            txt = txt.substr(i + 1);
            i = -1;
        }
    }
    if(txt.size() > 0){
        res.push_back(txt);
    }
    int count = 0;
    for(int i = 'a'; i <= 'z'; i++){
        if(txt.find(to_string(i)) != string::npos){
            count++;
        }
    }
    res.push_back(to_string(count));
    return res;
}
int main(){
    string txt = "Hello,world!";
    vector<string> res = split_words(txt);
    for(int i = 0; i < res.size(); i++){
        printf("%s\n", res[i].c_str());
    }
    return 0;
}
