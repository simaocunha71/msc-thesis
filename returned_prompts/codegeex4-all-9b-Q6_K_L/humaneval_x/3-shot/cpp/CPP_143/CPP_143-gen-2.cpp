    string result="";
    string current_word="";
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            if (is_prime(current_word.length()))
            {
                result+=current_word;
                result+=' ';
            }
            current_word="";
        }
        else
            current_word+=sentence[i];
    }
    if (is_prime(current_word.length()))
        result+=current_word;
    return result;
}
int is_prime(int num){
    if (num==1)
        return 0;
    int i;
    for (i=2;i<num;i++)
        if (num%i==0)
            return 0;
    return 1;
}