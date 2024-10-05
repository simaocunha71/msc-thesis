    string encrypted = "";
    for(int i = 0; i < s.length(); i++){
        int ascii = (int)s[i];
        if(ascii >= 65 && ascii <= 90){
            encrypted += (char)((((ascii - 65 + 2*2)%26)+65));
        }else if(ascii >= 97 && ascii <= 122){
            encrypted += (char)((((ascii - 97 + 2*2)%26)+97));
        }else{
            encrypted += s[i];
        }
    }
    return encrypted;
}

int main(){
    printf("%s\n", encrypt("hi").c_str());
    printf("%s\n", encrypt("asdfghjkl").c_str());
    printf("%s\n", encrypt("gf").c_str());
    printf("%s\n", encrypt("et").c_str());

    return 0;
}

*/

// --------------------------------------
// SOLUTION 3
// --------------------------------------
