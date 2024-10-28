    string new_sentence = "";
    string word;
    int i = 0;
    while(sentence[i] != ' '){
        word += sentence[i];
        i++;
    }
    if(isPrime(word.size())){
        new_sentence += word;
        i++;
    }
    else{
        goto A;
    }
    for(int j = i; j < sentence.size(); j++){
        if(sentence[j] == ' '){
            i = j + 1;
            while(sentence[i] != ' '){
                word += sentence[i];
                i++;
            }
            if(isPrime(word.size())){
                new_sentence += word;
                i++;
            }
            else{
                goto A;
            }
        }
    }
    return new_sentence;
}
int isPrime(int n){
    if(n == 2 || n == 3){
        return 1;
    }
    else if(n == 1 || n % 2 == 0 || n % 3 == 0){
        return 0;
    }
    else{
        for(int i = 5; i * i <= n; i += 6){
            if(n % i == 0 || n % (i + 2) == 0){
                return 0;
            }
        }
        return 1;
    }
}
int main(){
    string sentence = "This is a test";
    string new_sentence = words_in_sentence(sentence);
    printf("%s", new_sentence.c_str());
    return 0;
}
