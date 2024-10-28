        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
        for (String word : words) {
            int count = 0;
            for (int i = 0; i < word.length(); i++) {
                if (consonants.indexOf(word.charAt(i)) != -1) count++;
            }
            if (count == n) result.add(word);
        }
        return result;
    }
}


A: Your solution is correct. 

But, I have one suggestion. The method `split` in Java splits on each occurrence of the specified delimiter, in your case it is space. It will consider multiple spaces as well as one space at the start or end of the string. So, if you have a string like "Hello   world", it will consider "Hello", " ", ""(empty string), "world" as words. 

If you want to handle multiple spaces, you should use a regex that matches one or more spaces.

Here is the modified code:

```java
public List<String> selectWords(String s, int n)  {
    List<String> result = new ArrayList<>();
    String[] words = s.split("\\s+");
    String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    for (String word : words) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (consonants.indexOf(word.charAt(i)) != -1) count++;
        }
        if (count == n) result.add(word);
    }
    return result;
}
```

The regular expression `\\s+` matches any number of space characters.

In this modified code, `split("\\s+")` will split the string `s` into words considering multiple spaces as a single space.


A: Here