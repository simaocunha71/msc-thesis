string encryptedString = "";
    for(int i = 0; i < s.size(); i++){
        char c = s[i];
        if(isupper(c)){
            encryptedString += char(((c - 'A' + 2 * 2) % 26) + 'A');
        }
        else{
            encryptedString += char(((c - 'a' + 2 * 2) % 26) + 'a');
        }
    }
    return encryptedString;
}

int main(){
    string s;
    printf("Enter the string: ");
    cin >> s;
    printf("Encrypted String: %s\n", encrypt(s).c_str());
    return 0;
}
*/

