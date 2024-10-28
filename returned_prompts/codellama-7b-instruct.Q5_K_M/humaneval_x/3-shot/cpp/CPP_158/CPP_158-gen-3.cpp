    sort(words.begin(),words.end());
    int max_unique=words[0].length();
    string max_word=words[0];
    for (int i=1;i<words.size();i++)
    if (words[i].length()>max_unique){
        max_unique=words[i].length();
        max_word=words[i];
    }
    return max_word;
}


