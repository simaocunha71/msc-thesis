    int flag=0;
    string s;
    int i,j,k;
    for(i=0;i<sentence.length();i++){
        if(sentence[i]==' '){
            if(flag==1){
                k=0;
                flag=0;
                continue;
            }
            else{
                flag=1;
            }
        }
        if(flag==0){
            s=s+sentence[i];
        }
    }
    return s;

}
int main(){
    string s="This is a test";
    cout<<words_in_sentence(s);
    return 0;
}
