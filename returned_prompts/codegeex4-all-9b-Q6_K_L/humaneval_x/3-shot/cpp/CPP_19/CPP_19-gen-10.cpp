
Code organization
You have included all of the code in your question.  It is best practice to separate the code into a main method and each of the functions.  This makes it easier to read and allows for easier testing of each function.  It also makes it possible to reuse the code in other programs.
Magic numbers
There are some magic numbers in the code.  These are numbers that are used but do not have a descriptive name.  It is best practice to replace these numbers with a named constant.  This makes it easier to understand what the code is doing.  For example, the number 9 in the following code is a magic number:
    num["zero"]=0;
    num["one"]=1;
    num["two"]=2;
    num["three"]=3;
    num["four"]=4;
    num["five"]=5;
    num["six"]=6;
    num["seven"]=7;
    num["eight"]=8;
    num["nine"]=9;

The number 9 should be replaced with a named constant like this:
    const int MAX_DIGITS = 9;

    num["zero"]=0;
