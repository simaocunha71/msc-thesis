Here is an alternative approach where we iterate over each character in the string, check if it's at an even index and if it's an uppercase vowel. We increment a counter if both conditions are met. 

This code utilizes the String method charAt(int index) to access each character in the string, the Character method isUpperCase(char ch) to check if the character is uppercase, and the String method contains(CharSequence s) to check if the character is an uppercase vowel. 

Finally, the method returns the count of uppercase vowels at even indices.

Here is the code:

```java
public int countUpper(String s) {
    int count = 0;
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(i % 2 == 0 && Character.isUpperCase(c) && "AEIOU".contains(String.valueOf(c))) {
            count++;
        }
    }
    return count;
}
```

This code works by iterating over each character in the string. If the character is at an even index and is an uppercase vowel, it increments the counter. Finally, it returns the count.

Here is an example of how to use this method:

```java
public static void main(String[] args) {
    Solution sol = new Solution();
    System.out.println(sol.countUpper("aBCdEf"));  // Outputs 1
    System.out.println(sol.countUpper("abcdefg"));  // Outputs 0
    System.out.println(sol.countUpper("dBBE"));  // Outputs 0
}