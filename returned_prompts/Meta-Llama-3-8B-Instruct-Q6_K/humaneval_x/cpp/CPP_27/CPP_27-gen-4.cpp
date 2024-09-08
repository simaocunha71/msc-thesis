    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = str[i] - 32;
        }
        else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = str[i] + 32;
        }
    }
    return str;
}

int main(){
    string s = "Hello";
    string result = filp_case(s);
    printf("%s\n", result.c_str());
    return 0;
}
