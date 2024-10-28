```java
public String encrypt(String s) {
    // create a string to store the encrypted string
    String encrypted = "";

    // iterate through each character in the string
    for (int i = 0; i < s.length(); i++) {
        // get the ASCII value of the character
        int ascii = (int) s.charAt(i);

        // if the character is a lowercase letter
        if (ascii >= 97 && ascii <= 122) {
            // shift the letter down by 2
            ascii += 2;

            // if the letter goes past 'z', wrap it around to 'a'
            if (ascii > 122) {
                ascii -= 26;
            }
        } 
        // if the character is an uppercase letter
        else if (ascii >= 65 && ascii <= 90) {
            // shift the letter down by 2
            ascii += 2;

            // if the letter goes past 'Z', wrap it around to 'A'
            if (ascii > 90) {
                ascii -= 26;
            }
        }

        // add the encrypted character to the string
        encrypted += (char) ascii;
    }

    return encrypted;
}
```