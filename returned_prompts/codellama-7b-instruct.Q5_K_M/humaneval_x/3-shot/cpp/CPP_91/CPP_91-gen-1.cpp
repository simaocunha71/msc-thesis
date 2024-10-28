    int i;
    int count=0;
    string current_sentence;
    int sentence_break;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='?'||S[i]=='!'||S[i]=='.')
        {
        sentence_break=i;
        current_sentence=S.substr(0,sentence_break);
        if (current_sentence.find("I")!=string::npos)
        count+=1;
        S=S.substr(sentence_break+1,S.length()-sentence_break);
        }
    }
    return count;
}



