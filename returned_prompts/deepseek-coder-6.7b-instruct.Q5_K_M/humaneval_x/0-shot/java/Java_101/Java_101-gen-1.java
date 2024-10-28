        List<String> words = new ArrayList<String>();
        String[] splitWords = s.split("[ ,]+");
        words = Arrays.asList(splitWords);
        return words;
    }
}

This solution uses Java's built-in split function of the String class. The split function takes a regular expression as an argument, which is used to divide the string. In this case, we use "[ ,]+" to split the string at spaces and commas. The "+" sign indicates one or more of the preceding element. 

Finally, we convert the resulting array of strings into a List and return it.

The complexity of this solution is O(n), where n is the length of the string. This is because we must go through the string once to split it into words.

The space complexity of this solution is also O(n), as we are storing each word in a new string in the array. In the worst case, every character in the string could be a separate word.

The solution assumes that the input string is well-formed and does not contain any invalid characters. In a real-world situation, you would want to add error checking to handle edge cases.

This solution works in the Java language.

It can be tested in an online Java compiler such as https://www.jdoodle.com/online-java-compiler or any other Java IDE.

When you run the given function with an input string "Hi, my name is John", it will return the array of strings ["Hi", "my", "name", "is", "John"]. Similarly, for the input string "One, two, three, four, five, six" it will return ["One", "two", "three", "four", "five", "six"].

Please note that the solution is case sensitive. So, 'Hi' and 'hi' would be treated as two different words.
    */

}





















































































