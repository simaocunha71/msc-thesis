    if(s.length()<3)
        return false;
    for(int i=0;i<s.length()-2;i++){
        if(s[i]==s[i+1] || s[i]==s[i+2] || s[i+1]==s[i+2])
            return false;
    }
    return true;
}

int main(){
    string s;
    printf("Enter the string: ");
    getline(cin, s);
    if(is_happy(s))
        printf("%s is a happy string.\n", s.c_str());
    else
        printf("%s is not a happy string.\n", s.c_str());
    return 0;
}