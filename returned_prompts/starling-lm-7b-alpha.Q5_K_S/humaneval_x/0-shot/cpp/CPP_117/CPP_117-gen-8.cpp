    vector<string> res;
    int len=s.length();
    int j;
    for(int i=0;i<len;i++){
        if(s[i]==' '){
            j=i;
            while(j<len&&s[j]==' '){
                j++;
            }
            if((j-i+1)-count(s.begin()+i,s.begin()+j,('b'||'c'||'d'||'f'||'g'||'h'||'j'||'k'||'l'||'m'||'n'||'p'||'q'||'r'||'s'||'t'||'v'||'w'||'x'||'z'))>0&&(j-i+1)-count(s.begin()+i,s.begin()+j,('a'||'e'||'i'||'o'||'u'))==n)
                res.push_back(s.substr(i,j-i+1));
        }
    }
    return res;
}


int main(){
    string s;
    int n;
    cin>>s>>n;
    vector<string> res;
    res=select_words(s,n);
    for(int i=0;i<res.size();i++)
        cout<<res[i]<<" ";
    return 0;
}






































































































































































