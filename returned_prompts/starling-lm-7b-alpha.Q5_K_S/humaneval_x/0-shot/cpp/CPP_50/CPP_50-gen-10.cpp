
int main() {
    string s="";
    printf("Enter the string to encode: ");
    fgets(s.c_str(),100,stdin);
    printf("Encoded string is: %s\n",encode_shift(s).c_str());
    printf("Enter the encoded string to decode: ");
    fgets(s.c_str(),100,stdin);
    printf("Decoded string is: %s\n",decode_shift(s).c_str());
    return 0;
}

To encode the string, you can use the following function:

string encode_shift(string s){
    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+5-(int)'a')%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}

To decode the string, you can use the following function:

string decode_shift(string s){
    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+(int)'a'-5)%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}

In the above functions, we are shifting every character by 5 in the alphabet. For example, 'a' becomes 'f', 'b' becomes 'g' and so on.

Here is the step-by-step explanation of the encode function:

1. Initialize an empty string called "out" to store the encoded string.
2. Loop through each character in the input string "s".
3. For each character, calculate the new character by adding 5 to the ASCII value of the character and then taking the modulo 26. This ensures that the character does not go out of the range of lowercase alphabets.
4. Convert the calculated ASCII value back to a character and add it to the "out" string.
5. Repeat steps 2-4 for all characters in the input string.