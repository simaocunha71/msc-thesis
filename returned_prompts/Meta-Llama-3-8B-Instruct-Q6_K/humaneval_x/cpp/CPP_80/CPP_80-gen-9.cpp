    if(s.length() < 3){
        return false;
    }
    for(int i = 0; i < s.length() - 2; i++){
        string substr = s.substr(i, 3);
        if(substr.length() != 3 || substr.find(substr[0]) != string::npos || substr.find(substr[1]) != string::npos || substr.find(substr[2]) != string::npos){
            return false;
        }
    }
    return true;
}
int main(){
    string s;
    printf("Enter a string: ");
    getline(cin, s);
    if(is_happy(s)){
        printf("%s is happy.\n", s.c_str());
    }
    else{
        printf("%s is not happy.\n", s.c_str());
    }
    return 0;
}

