    vector<string> words;
    string word;
    int i;
    int count=0;
    for(i=0;i<txt.size();i++){
        if(txt[i]==' '||txt[i]==','){
            if(!word.empty()){
                words.push_back(word);
                word="";
            }
        }
        else{
            word+=txt[i];
            if(txt[i]>='a'&&txt[i]<='z'){
                if((txt[i]-'a')%2==1)
                    count++;
            }
        }
    }
    if(!word.empty())
        words.push_back(word);
    if(count>0)
        words.push_back(to_string(count));
    return words;
}


