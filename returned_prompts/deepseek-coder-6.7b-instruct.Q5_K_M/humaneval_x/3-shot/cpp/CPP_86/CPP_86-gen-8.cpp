    string word = "";
    string result = "";
    for (char &c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + " ";
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}


