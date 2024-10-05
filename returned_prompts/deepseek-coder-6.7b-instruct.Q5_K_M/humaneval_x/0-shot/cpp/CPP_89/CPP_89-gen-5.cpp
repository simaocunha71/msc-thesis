    string encrypted = "";

    for(int i = 0; i < s.length(); i++){
        char c = s[i];
        if(isupper(c)){
            encrypted += char(int(c + (2 * 2)) % 26 + 65);
        }else{
            encrypted += char(int(c + (2 * 2)) % 26 + 97);
        }
    }

    return encrypted;
}

int main(){
    printf("%s", encrypt("hi").c_str());
    return 0;
}

*/

