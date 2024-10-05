    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            continue;
        }
        else{
            char c=s[i];
            char d;
            int n=s.size();
            for(int j=i;j<n;j++){
                d=s[j];
                if(d<c){
                    c=d;
                }
            }
            for(int j=i;j<n;j++){
                d=s[j];
                if(d==c){
                    s[j]=s[i];
                    s[i]=c;
                    goto A;
                }
            }
        }
    }
    return s;
}
int main(){
    string s="Hello World!!!";
    printf("%s\n",anti_shuffle(s).c_str());
    return 0;
}



























































































































































































































































































