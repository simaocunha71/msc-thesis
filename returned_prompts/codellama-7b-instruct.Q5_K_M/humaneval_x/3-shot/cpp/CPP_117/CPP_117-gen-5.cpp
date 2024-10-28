    vector<string> all_words;
    int i=0;
    string current_word;
    while (i<s.length()){
        while (s[i]==' '){
            i++;
        }
        int j=i;
        while (s[j]!=' ' && j<s.length()){
            j++;
        }
        current_word=s.substr(i,j-i);
        int consonant_count=0;
        for (int k=0;k<current_word.length();k++)
        if (current_word[k]!='a' && current_word[k]!='e' && current_word[k]!='i' && current_word[k]!='o' && current_word[k]!='u'){
            consonant_count+=1;
        }
        if (consonant_count==n){
            all_words.push_back(current_word);
        }
        i=j;
    }
    return all_words;
}


