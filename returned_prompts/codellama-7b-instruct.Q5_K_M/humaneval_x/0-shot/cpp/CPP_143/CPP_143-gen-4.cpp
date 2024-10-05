    string result="";
    for(int i=0;i<sentence.length();i++){
        if(sentence[i]==' '){
            goto B;
        }
        result+=sentence[i];
    }
    B:
    bool prime[100]={false};
    prime[0]=true;
    prime[1]=true;
    for(int i=2;i<100;i++){
        if(prime[i]) continue;
        for(int j=2;j*i<100;j++){
            prime[i*j]=true;
        }
    }
    string word="";
    for(int i=0;i<result.length();i++){
        if(result[i]==' '){
            if(prime[word.length()]){
                word+=result[i];
            }
            continue;
        }
        word+=result[i];
    }
    return word;
}
int main(){
    string sentence="This is a test";
    printf("%s\n", words_in_sentence(sentence).c_str());
    return 0;
}
