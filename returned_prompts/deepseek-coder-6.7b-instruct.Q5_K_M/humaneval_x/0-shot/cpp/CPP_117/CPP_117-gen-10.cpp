    vector<string> result;
    vector<string> words;
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            words.push_back(temp);
            temp="";
        }
        else{
            temp+=s[i];
        }
    }
    words.push_back(temp);
    for(int i=0;i<words.size();i++){
        int count=0;
        for(int j=0;j<words[i].length();j++){
            char c=tolower(words[i][j]);
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                continue;
            }
            else{
                count++;
            }
        }
        if(count==n){
            result.push_back(words[i]);
        }
    }
    return result;
}
int main() {
    vector<string> result=select_words("Mary had a little lamb",4);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<" ";
    }
    return 0;
}

Output:
little 
*/




























































































































































































