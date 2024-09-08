    string result = "";
    for(int i = 0; i < s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    return result;
}

int main(){
    printf("%s\n", solve("1234").c_str());
    printf("%s\n", solve("ab").c_str());
    printf("%s\n", solve("#a@C").c_str());
    return 0;
}
