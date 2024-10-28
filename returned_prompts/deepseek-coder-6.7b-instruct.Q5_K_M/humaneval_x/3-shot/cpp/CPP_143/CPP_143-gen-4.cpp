    string word,res;
    stringstream ss(sentence);
    while(ss >> word){
        int len = word.length();
        if(len == 2 || len == 3){
            res += word + " ";
        }
    }
    return res;
}



