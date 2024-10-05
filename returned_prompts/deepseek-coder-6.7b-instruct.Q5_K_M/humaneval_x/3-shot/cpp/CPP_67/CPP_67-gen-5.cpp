    int apples = 0, oranges = 0, mangoes = 0;
    string temp = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' '){
            if(temp == "apples")
                apples = stoi(s.substr(0, i));
            else if(temp == "oranges")
                oranges = stoi(s.substr(0, i));
            temp = "";
        }
        else
            temp += s[i];
    }
    mangoes = n - apples - oranges;
    return mangoes;
}


