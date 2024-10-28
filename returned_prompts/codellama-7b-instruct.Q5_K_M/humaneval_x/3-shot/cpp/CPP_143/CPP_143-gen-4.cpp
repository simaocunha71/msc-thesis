    string words[50];
    int count=0;
    int i=0;
    int j=0;
    int k=0;
    for (i=0;i<sentence.length();i++){
        if (sentence[i]==' '){
            words[k]=sentence.substr(j,i-j);
            count++;
            j=i+1;
            k++;
        }
    }
    words[k]=sentence.substr(j,i-j);
    count++;

    string result="";
    for (i=0;i<count;i++){
        if (is_prime(words[i].length())){
            result+=words[i];
        }
    }
    return result;
}
bool is_prime(int x){
    if (x==0||x==1||x==2)
    return false;
    int i;
    for (i=2;i<x;i++)
    if (x%i==0)
    return false;
    return true;
}


