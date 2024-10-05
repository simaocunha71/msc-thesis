    vector<string> words;
    int i,j;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' '){
            for (j=0;j<i;j++)
            words.push_back(sentence.substr(j,i-j));
        }
    }
    for (i=0;i<words.size();i++)
    if (words[i].length()!=2 && words[i].length()!=3 && words[i].length()!=5 && words[i].length()!=7 && words[i].length()!=11 && words[i].length()!=13 && words[i].length()!=17 && words[i].length()!=19 && words[i].length()!=23 && words[i].length()!=29 && words[i].length()!=31 && words[i].length()!=37 && words[i].length()!=41 && words[i].length()!=43 && words[i].length()!=47 && words[i].length()!=53 && words[i].length()!=59 && words[i].length()!=71 && words[i].length()!=73 && words[i].length()!=79 && words[i].length()!=83 && words[i].length()!=89 && words[i].length()!=97 && words[i].length()!=101 && words[i].length()!=103 && words[i].length()!=107 && words[i].length()!=109 && words[i].length()!=113 && words[i].length()!=127 && words[i].length()!=131 && words[i].length()!=137 && words[i].length()!=139 && words[i].length()!=149 && words[i].length()!=151 && words[i].length()!=157 && words[i].length()!=167 && words[i].length()!=173 && words[i].length()!=179 && words[i].length()!=181 && words[i].