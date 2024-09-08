    string res = "";
    string word;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == ' ') {
            res += word + " ";
            word = "";
        } else {
            word += s[i];
        }
    }
    res += word;

    for(int i = 0; i < res.length(); i++) {
        if(res[i] == ' ') {
            res = res.substr(0, i) + " " + res.substr(i+1);
        }
    }

    for(int i = 0; i < res.length(); i++) {
        if(res[i] != ' ') {
            string temp = res.substr(i,1);
            char c = temp[0];
            string new_word = "";
            for(int j = 0; j < temp.length(); j++) {
                if(temp[j] < c) {
                    new_word += temp[j];
                }
            }
            res.replace(i,1,new_word);
            i += new_word.length() - 1;
        }
    }
    return res;
}

int main() {
    string s = "Hello World!!!";
    cout << anti_shuffle(s) << endl;
    return 0;
}

