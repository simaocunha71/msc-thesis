    string res = "";
    int i = 0;
    while(i<s.length()){
        string temp = "";
        while(i<s.length() && s[i] != ' '){
            temp += s[i];
            i++;
        }
        if(temp.length() > 0){
            sort(temp.begin(), temp.end());
            res += temp;
        }
        if(i<s.length()){
            res += " ";
            i++;
        }
    }
    return res;
}
