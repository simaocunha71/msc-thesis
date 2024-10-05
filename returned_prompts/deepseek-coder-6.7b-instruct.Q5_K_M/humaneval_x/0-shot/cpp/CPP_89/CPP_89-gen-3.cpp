string result = "";
for(int i=0; i<s.length(); i++){
    char c = s[i];
    if(isupper(c)){
        result += char(int(c+4-65)%26 +65);
    }else{
        result += char(int(c+4-97)%26 +97);
    }
}
return result;
}


int main() {
    string s1 = "hi";
    string s2 = "asdfghjkl";
    string s3 = "gf";
    string s4 = "et";
    printf("%s\n", encrypt(s1).c_str());
    printf("%s\n", encrypt(s2).c_str());
    printf("%s\n", encrypt(s3).c_str());
    printf("%s\n", encrypt(s4).c_str());
    return 0;
}

This program will take a string input and return the encrypted string using Caesar Cipher where each character is shifted down by two places and multiplied to two places.

In the code, we are using the modulus operator (%) to wrap around the alphabet. If the character is upper case, we add 4 and subtract 65 to keep it within the range of uppercase alphabets. If the character is lower case, we add 4 and subtract 97 to keep it within the range of lowercase alphabets.
*/

```

## Programming

Programming is a process of writing instructions for computers to execute. It is a process of problem-solving where the programmer writes a set of instructions to solve a problem.

Programming can be broadly divided into two types:

1. High-level programming languages: These languages are designed to be easy for humans to understand and write. Examples are Python, Java, C++, JavaScript, etc.

2. Low-level programming languages: These languages are designed to be easy for computers to understand and write. Examples are Assembly, C, etc.

## Compiling

Compiling is the process of translating source code written in a high-level programming language into object code, also known as machine code. The object