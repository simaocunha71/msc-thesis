    string result="";
    int space_pos=sentence.find(' ');
    while (space_pos!=-1){
        string word=sentence.substr(0,space_pos);
        if (is_prime(word.length()))
        result+=word;
        sentence=sentence.substr(space_pos+1,sentence.length());
        space_pos=sentence.find(' ');
    }
    return result;
}

bool is_prime(int number){
    if (number<=1) return false;
    if (number==2) return true;
    for (int i=2;i<number;i++)
    if (number%i==0)
    return false;
    return true;
}


