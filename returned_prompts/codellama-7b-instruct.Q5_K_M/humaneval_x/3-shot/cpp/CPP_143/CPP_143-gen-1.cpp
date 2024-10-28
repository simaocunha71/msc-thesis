    int i,j;
    string prime_words="";
    string all_words[101];
    int all_words_len[101];
    string word;
    int prime_word_len;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            word=sentence.substr(j,i-j);
            all_words[all_words_len[i]]=word;
            j=i+1;
        }
    }
    word=sentence.substr(j,i-j);
    all_words[all_words_len[i]]=word;
    for (i=0;i<101;i++)
    {
        prime_word_len=all_words[i].length();
        if (prime_word_len==0)
        break;
        if (prime_word_len>1)
        {
        if (prime_word_len%2==0)
        continue;
        }
        prime_words+=all_words[i];
    }
    return prime_words;
}


