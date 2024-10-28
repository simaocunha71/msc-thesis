    vector<string> words;
    string word = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ',' || s[i] == ' '){
            if(word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += s[i];
        }
    }
    if(word != ""){
        words.push_back(word);
    }
    return words;
}

int main()
{
    vector<string> words = words_string("Hi, my name is John");
    for(int i=0; i<words.size(); i++){
        printf("%s\n", words[i].c_str());
    }
    return 0;
}


A: The task is to split a string into words by comma or space. 
The problem here is that it is not specified if commas are optional. If they are not optional, then you need to take care of them.

