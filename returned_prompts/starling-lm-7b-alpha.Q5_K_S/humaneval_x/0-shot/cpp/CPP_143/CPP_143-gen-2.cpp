    string res;
    for(char c:sentence){
        if(isalpha(c)){
            res+=c;
        }
    }
    if(res.size()==0){
        return res;
    }
    if(res[0]==' '){
        return res.substr(1);
    }
    if(res.back()==' '){
        return res.substr(0,res.size()-1);
    }
    int len=res.size();
    for(int i=2;i<=len;i++){
        if(i==2){
            if(len%i==0){
                if(len%2==1){
                    res.pop_back();
                }else{
                    res.pop_front();
                }
                continue A;
            }else{
                continue;
            }
        }
        bool prime=true;
        for(int j=2;j*j<=i;j++){
            if(i%j==0){
                prime=false;
                break;
            }
        }
        if(prime){
            if(len%i==0){
                if(len%2==1){
                    res.pop_back();
                }else{
                    res.pop_front();
                }
                continue A;
            }else{
                continue;
            }
        }
    }
    return res;
}
int main(){
    string s;
    cin>>s;
    cout<<words_in_sentence(s);
}


































































































































