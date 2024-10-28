    int i,j;
    int max_unique_char_count=0;
    string max_unique_char_word;
    for (i=0;i<words.size();i++)
    {
        int curr_unique_char_count=0;
        for (char chr='a'; chr<='z'; chr++)
        if (find(words[i].begin(), words[i].end(), chr)!=words[i].end())
            curr_unique_char_count+=1;

        if (curr_unique_char_count>max_unique_char_count){
            max_unique_char_count=curr_unique_char_count;
            max_unique_char_word=words[i];
        }
    }
    return max_unique_char_word;
}



