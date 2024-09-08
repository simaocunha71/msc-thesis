    string result = "";
    for(int i = 0; i < message.length(); i++){
        char c = message[i];
        if(islower(c)){
            result += toupper(c);
        }else if(isupper(c)){
            result += tolower(c);
        }else{
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                    result += (char)(c + 2);
                }
            }else{
                result += c;
            }
        }
    }
    return result;
}

int main(){
    printf("%s\n", encode("test"));
    printf("%s\n", encode("This is a message"));
    return 0;
}
```

