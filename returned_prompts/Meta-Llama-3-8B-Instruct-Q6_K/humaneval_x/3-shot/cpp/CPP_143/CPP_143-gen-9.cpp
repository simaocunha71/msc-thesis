    string result;
    string word;
    for (int i=0;i<sentence.length();i++){
        if (sentence[i]==' '){
            if (is_prime(word.length())){
                result+=word+" ";
            }
            word="";
        }else{
            word+=sentence[i];
        }
    }
    if (is_prime(word.length())){
        result+=word;
    }
    return result.trim();
}

bool is_prime(int n){
    if (n<2) return false;
    for (int i=2;i*i<=n;i++)
    {
        if (n%i==0)
            return false;
    }
    return true;
}
string trim(const string& str) {
    size_t start = str.find_first_not_of(' ');
    size_t end = str.find_last_not_of(' ');
    return str.substr(start, (end-start+1));
}

