    vector<string> words;
    string temp_word = "";
    int count = 0;

    for(auto chr : txt){
        if(chr == ' ' || chr == ','){
            if(!temp_word.empty()){
                words.push_back(temp_word);
                temp_word = "";
            }
        }else{
            temp_word += chr;
            if(islower(chr)) count++;
        }
    }

    if(!temp_word.empty()){
        words.push_back(temp_word);
    }

    if(words.empty()){
        words.push_back(to_string(count % 2 == 1 ? count : 0));
    }

    return words;
}


