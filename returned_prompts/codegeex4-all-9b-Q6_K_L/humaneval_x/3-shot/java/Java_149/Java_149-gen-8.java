
You have a few good things going on in your code.  Let's take a look at some of the things we can do to make it better.

Comments
I'd say that comments are used well here.  They're brief and clear.  However, they're not always necessary.  For example, in your first code snippet, you have the following comment:

/**
Check if in given list of numbers, are any two numbers closer to each other than given threshold.
>>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
false
>>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
true
 */

This comment is redundant with the function name and the Javadoc comments.  It's better to focus on what the function does, not how it does it.  In this case, the Javadoc comments already tell us what the function does, and the function name makes it clear that it's a boolean function.

Naming
Your function names are clear and descriptive.  That's good.  However, you've used the prefix "list" in your function names, which is unnecessary.  In Java, it's common to use prefixes to indicate the type of the parameter or return value, but not to indicate the type of the function itself.  So, you could change your function names to something like this:

public boolean hasCloseNumbers(List<Double> numbers, double threshold) {
    // ...
}

public List<String> separateParenGroups(String parenString) {
    // ...
}

public double truncateNumber(double number) {
    // ...
}

public List<String> listSort(List<String> lst) {
    // ...
}

You might also consider using more descriptive names for your variables.  For example, in your second function, you have the following variables:

List<String> result = new ArrayList<>();
StringBuilder currentString = new StringBuilder();
int currentDepth = 0;

These names are clear, but you could consider using more descriptive names, like this:

List<String> groups = new ArrayList<>();
StringBuilder currentGroup = new StringBuilder();
int depth = 0;

This makes it clear that "result" is a list of groups, "currentString" is a string