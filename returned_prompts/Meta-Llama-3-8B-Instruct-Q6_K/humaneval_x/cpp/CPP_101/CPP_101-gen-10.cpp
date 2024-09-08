    vector<string> res;
    int i = 0;
    while(i < s.length()){
        if(s[i] == ' ' || s[i] == ','){
            res.push_back(s.substr(i+1, s.find(s[i], i+1) - i - 1));
            i = s.find(s[i], i+1);
        } else {
            i++;
        }
    }
    res.push_back(s.substr(i));
    return res;
}
B:
    vector<string> res;
    string word;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' ' || s[i] == ','){
            res.push_back(word);
            word = "";
        } else {
            word += s[i];
        }
    }
    res.push_back(word);
    return res;
}
C:
    vector<string> res;
    string word = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' ' || s[i] == ','){
            res.push_back(word);
            word = "";
        } else {
            word += s[i];
        }
    }
    res.push_back(word);
    return res;
}D:
    vector<string> res;
    string word = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' ' || s[i] == ','){
            res.push_back(word);
            word = "";
            i++;
        } else {
            word += s[i];
        }
    }
    res.push_back(word);
    return res;
}
E:
    vector<string> res;
    string word = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' ' || s[i] == ','){
            res.push_back(word);
            word = "";
        } else {
            word += s[i];
        }
    }
    res.push_back(word);
    return res;
}

int main()
{
    string s = "Hi, my name is John";
    vector<string> res = words_string(s);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << endl;
    }
    return 0;
}

I:
The function words_string() takes a string s as input and returns a vector of strings. It uses a loop to iterate over the characters in the string. If the character is a space or a comma