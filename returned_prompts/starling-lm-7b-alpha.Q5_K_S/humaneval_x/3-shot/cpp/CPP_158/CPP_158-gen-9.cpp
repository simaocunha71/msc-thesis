    vector<string> all_unique;
    string max_word;
    int max_len=0;
    int i;
    for (i=0;i<words.size();i++)
    {
        string current_word=words[i];
        sort(current_word.begin(),current_word.end());
        if (current_word.length()>max_len){
            max_word=current_word;
            max_len=current_word.length();
        }
    }
    return max_word;
}




