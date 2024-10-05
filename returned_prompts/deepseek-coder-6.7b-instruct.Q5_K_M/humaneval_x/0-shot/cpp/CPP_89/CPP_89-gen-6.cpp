  for(int i=0;s[i];i++){
    if(s[i]>='a' && s[i]<='z'){
      s[i]=((s[i]-'a'+2*2)%26)+'a';
    }
    else if(s[i]>='A' && s[i]<='Z'){
      s[i]=((s[i]-'A'+2*2)%26)+'A';
    }
  }
  return s;
}

int main() {
    printf("%s\n", encrypt("hi").c_str());
    printf("%s\n", encrypt("asdfghjkl").c_str());
    printf("%s\n", encrypt("gf").c_str());
    printf("%s\n", encrypt("et").c_str());
    return 0;
}

Answer:
The function encrypt takes a string as an argument and returns the same string 
but with every alphabet character shifted down by two places and multiplied to two places.
The characters that are shifted out of the lowercase or uppercase alphabet range are 
wrapped around to the start of the alphabet.
The function uses a for loop to go through every character in the string.
If a character is a lowercase letter, it is shifted down by two places and multiplied to two places
and then wrapped around to the start of the alphabet if it goes past 'z'.
If a character is an uppercase letter, it is shifted down by two places and multiplied to two places
and then wrapped around to the start of the uppercase alphabet if it goes past 'Z'.
If the character is not an alphabet, it is not shifted and remains the same.
The shifted string is then returned.
*/

// End of Solution

// End of Program










































































