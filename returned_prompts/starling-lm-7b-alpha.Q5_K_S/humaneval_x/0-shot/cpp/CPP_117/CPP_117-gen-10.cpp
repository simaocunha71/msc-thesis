    vector<string> result;
    bool isConsonant[30];
    for(int i=0;i<30;i++)
        isConsonant[i]=false;
    for(int i=0;i<30;i++)
        isConsonant[i]=true;
    isConsonant[' ']=false;
    isConsonant['.']=false;
    isConsonant[',']=false;
    isConsonant['?']=false;
    isConsonant['!']=false;
    isConsonant[':']=false;
    isConsonant[';']=false;
    isConsonant['\'']=false;
    isConsonant['\'']=false;
    isConsonant['\'']=false;
    isConsonant['\'']=false;
    int consonantCount=0;
    string tmp;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            if(consonantCount==n){
                tmp.clear();
                result.push_back(tmp);
                tmp=string();
            }else if(consonantCount<n){
                tmp.clear();
                result.push_back(tmp);
            }
            consonantCount=0;
        }else if(s[i]=='\0'){
            if(consonantCount==n){
                tmp.clear();
                result.push_back(tmp);
                tmp=string();
            }else if(consonantCount<n){
                tmp.clear();
                result.push_back(tmp);
            }
            consonantCount=0;
        }else{
            if(isConsonant[s[i]]==true){
                tmp+=s[i];
                consonantCount++;
            }
        }
    }
    return result;
}
int main(){
    string s;
    int n;
    cin>>s>>n;
    vector<string> result=select_words(s,n);