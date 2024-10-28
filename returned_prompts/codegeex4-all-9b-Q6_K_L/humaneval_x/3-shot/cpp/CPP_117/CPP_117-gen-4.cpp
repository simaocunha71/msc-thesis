    vector<string> words;
    vector<char> consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
    string current_word="";
    int consonant_count=0;
    for (int i=0;i<s.length();i++){
        if (s[i]==' '){
            if (consonant_count==n)
                words.push_back(current_word);
            current_word="";
            consonant_count=0;
        }
        else{
            current_word+=s[i];
            for (int j=0;j<consonants.size();j++)
            if (s[i]==consonants[j])
                consonant_count+=1;
        }
    }
    return words;
}

