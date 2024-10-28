    int max_unique = -1;
    string max_word = "";
    for(auto word : words){
        int unique_count = distance(string(word.begin(), unique(word.begin(), word.end())), word.end());
        if(unique_count > max_unique){
            max_unique = unique_count;
            max_word = word;
        }
        else if(unique_count == max_unique){
            if(word < max_word)
                max_word = word;
        }
    }
    return max_word;
}


