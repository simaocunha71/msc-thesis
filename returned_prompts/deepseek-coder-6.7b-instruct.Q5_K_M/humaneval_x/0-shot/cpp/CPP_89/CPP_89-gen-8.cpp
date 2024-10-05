string encrypted = "";
for(int i=0; i<s.size(); i++){
    if(s[i] >= 'a' && s[i] <= 'z'){
        encrypted += (char)((((s[i] - 'a') + 2 * 2) % 26) + 'a');
    }else if(s[i] >= 'A' && s[i] <= 'Z'){
        encrypted += (char)((((s[i] - 'A') + 2 * 2) % 26) + 'A');
    }else{
        encrypted += s[i];
    }
}
return encrypted;
}
int main(){
string s;
printf("Enter a string:\n");
getline(cin, s);
string encrypted = encrypt(s);
printf("Encrypted string: %s\n", encrypted.c_str());
return 0;
}

*/

#include <stdio.h>
#include <string.h>

char* encrypt(char* str){
    int len = strlen(str);
    static char encrypted[100];
    for(int i = 0; i < len; i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            encrypted[i] = (((str[i] - 'a') + 2 * 2) % 26) + 'a';
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            encrypted[i] = (((str[i] - 'A') + 2 * 2) % 26) + 'A';
        }else{
            encrypted[i] = str[i];
        }
    }
    encrypted[len] = '\0';
    return encrypted;
}

int main(){
    char str[100];
    printf("Enter a string:\n");
    fgets(str, sizeof(str), stdin);
    if(str[strlen(str)-1] == '\n') str[strlen(str)-1] = '\0';
    char* encrypted = encrypt(str);
   