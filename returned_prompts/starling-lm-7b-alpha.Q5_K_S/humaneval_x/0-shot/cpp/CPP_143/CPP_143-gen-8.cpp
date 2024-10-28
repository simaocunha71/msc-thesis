    int len=sentence.length();
    string ans="";
    int i=0;
    while(i<len){
        int j=0;
        while(i+j<len){
            if(j==0){
                for(int k=0;k<len;++k){
                    if(sentence[i+k]==' '){
                        ++k;
                        break;
                    }
                    if(sentence[i+k]=='\0'){
                        break;
                    }
                    ans+=sentence[i+k];
                }
                if(ans.length()!=0){
                    j++;
                }
            }
            else{
                for(int k=0;k<len;++k){
                    if(sentence[i+j+k]==' '){
                        ++k;
                        break;
                    }
                    if(sentence[i+j+k]=='\0'){
                        break;
                    }
                    ans+=sentence[i+j+k];
                }
                if(ans.length()!=0){
                    j++;
                }
            }
        }
        if(ans.length()!=0&&isPrime(ans.length())){
            return ans;
        }
        else{
            ans="";
        }
        i+=j+1;
    }
    return ans;
}
bool isPrime(int x){
    if(x==2||x==3||x==5||x==7){
        return true;
    }
    if(x%2==0||x%3==0||x%5==0||x%7==0){
        return false;
    }
    for(int i=11;i*i<=x;i+=12){
        if(x%i==0||x%(i+2)==0){
            return false;
        }
    }
    return true;
}
int main(){
    string s;
    cin>>s;
    cout<<words_in_sentence(