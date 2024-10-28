        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5 - 'a' + 26) % 26)));
        }
        return sb.toString();
    }
}

What's wrong with this code?
I'm getting a compile error on line 13 (the line with 'A':) stating "illegal start of expression". The code compiles fine with the 'Q' and 'B' parts. 

A: Your problem is that you have defined two classes within one file and named them both Solution. In Java, you cannot have two classes in one file. Each class definition should be in its own file. 


*

*Move the second class definition to its own file. 

*Ensure that the file name matches the class name. 

*If you want to run the code, you would need to compile both files separately, not just the one with the main method.


Also, in your code, you are using 'A' instead of 'a'. Make sure you're using the correct case in your method names.

A: You have two classes in the same file which is causing the error. Java does not allow two classes to be defined in a single file.
You should have separate files for each class.
So, you should have two files:


*

*SolutionQ.java (for the class Solution defined at the start of your post)

*SolutionA.java (for the class Solution defined at the end of your post)


Then, you can compile them separately:


*

*javac SolutionQ.java

*javac SolutionA.java


A: You have two classes defined in your file, which is causing the error. You can't have two classes in a single file.
Separate them into two different files:


*

*SolutionQ.java (for the class Solution defined at the start of your post)

*SolutionA.java (for the class Solution defined at the end of your post)


Then, you can compile them separately:


*

*javac SolutionQ