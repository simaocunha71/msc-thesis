string encrypted = "";
    for (int i = 0; i < s.length(); i++){
        char c = s[i];
        if(isupper(c)){
            encrypted += char(int(c + (2 * 2)) % 26 + 65);
        }
        else{
            encrypted += char(int(c + (2 * 2)) % 26 + 97);
        }
    }
    return encrypted;
}

int main(){
    printf(encrypt("hi").c_str());
    return 0;
}

*/


A: The problem is in your character shifting. You are adding 2 to the ASCII value of each character and then taking modulo 26, but this doesn't actually rotate the alphabet, it just shifts it.
To rotate the alphabet, you need to add 2 to the ASCII value of each character and then take modulo 26, but the modulo should be 26, not 28.
Here's the corrected code:
string encrypt(string s){
    string encrypted = "";
    for (int i = 0; i < s.length(); i++){
        char c = s[i];
        if(isupper(c)){
            encrypted += char((c - 'A' + 2) % 26 + 'A');
        }
        else{
            encrypted += char((c - 'a' + 2) % 26 + 'a');
        }
    }
    return encrypted;
}

In this code, the expression (c - 'A' + 2) % 26 + 'A' calculates the ASCII value of the rotated character. This works because 'A' to 'Z' have ASCII values 65 to 90, and 'a' to 'z' have ASCII values 97 to 122.

A: The issue is that you're adding 2 to each character, but you should be multiplying it by 2, not adding.
Here is the corrected code:
string encrypt(string s){
    string encrypted = "";
    for (int i = 0; i < s.length(); i++){
        char c = s