    vector<string> words;
    string word;
    int i;
    int odd_count=0;
    for  (i=0;i<txt.length();i++)
    {
        if  (txt[i]==' '||txt[i]==',')
        {
            if  (!word.empty()){
                words.push_back(word);
            }
            word="";
        }
        else
        {
            if  (txt[i]>='a' && txt[i]<='z'){
                int pos=txt[i]-'a';
                if  ((pos+1)%2==1){
                    odd_count++;
                }
            }
            word+=txt[i];
        }
    }
    if  (!word.empty()){
        words.push_back(word);
    }
    if  (odd_count>0){
        words.push_back(to_string(odd_count));
    }
    return words;
}


