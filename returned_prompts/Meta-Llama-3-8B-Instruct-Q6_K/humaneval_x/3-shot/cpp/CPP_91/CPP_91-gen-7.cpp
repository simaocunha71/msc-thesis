    int count=0;
    int i;
    bool in_sentence=true;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]== '!'){
            in_sentence=false;
        }
        if (in_sentence && S[i]=='I'){
            count++;
            in_sentence=false;
        }
        if (!in_sentence && (S[i]=='.' || S[i]=='?' || S[i]== '!')){
            in_sentence=true;
        }
    }
    return count;
}