    string result = "";
    for(int i = 0; i < message.length(); i++){
        if(isalpha(message[i])){
            char c = tolower(message[i]);
            if(c >= 'a' && c <= 'z'){
                if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                    c += 2;
                    if(c > 'z') c -= 26;
                }
                result += (c >= 'a' ? 'a' + (c - 'a') : 'A' + (c - 'A'));
            }else{
                result += toupper(message[i]);
            }
        }else{
            result += message[i];
        }
    }
    return result;
}

int main(){
    string message = "This is a message";
    cout << encode(message) << endl;
    return 0;
}