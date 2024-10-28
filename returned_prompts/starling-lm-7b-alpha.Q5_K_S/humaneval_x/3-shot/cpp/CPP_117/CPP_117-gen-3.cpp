    vector<string> all_words;
    vector<string> current_words;
    string word;
    char chr;
    int vowels=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '){
        if (vowels==n)
        {
            all_words.push_back(word);
        }
        sort(current_words.begin(),current_words.end());
        if (current_words.size()>0 && word==current_words[current_words.size()-1])
        {
            current_words.pop_back();
        }
        word="";
        vowels=0;
        }
        else if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u')
        {
        vowels+=0;
        }
        else
        {
            word+=chr;
            vowels+=1;
        }
        if (i==s.length()-1)
        {
        if (vowels==n)
        {
            all_words.push_back(word);
        }
        sort(current_words.begin(),current_words.end());
        if (current_words.size()>0 && word==current_words[current_words.size()-1])
        {
            current_words.pop_back();
        }
        word="";
        vowels=0;
        }
        current_words.push_back(word);
    }
    return all_words;
}



