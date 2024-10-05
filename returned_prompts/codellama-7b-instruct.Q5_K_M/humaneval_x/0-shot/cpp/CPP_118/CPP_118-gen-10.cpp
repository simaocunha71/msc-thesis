    string::iterator iter = word.end();
    for(;iter != word.begin(); iter--){
        if(isalpha(*iter)){
            if(isvowel(*iter)){
                string::iterator next = iter;
                next--;
                if(!isalpha(*next) || isvowel(*next)){
                    return *iter;
                }
            }
        }
    }
    return "";
}



