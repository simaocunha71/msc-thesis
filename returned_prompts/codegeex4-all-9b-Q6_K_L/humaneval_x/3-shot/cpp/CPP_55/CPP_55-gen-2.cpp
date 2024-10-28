
The first thing you need to do is to remove the comments, the code doesn't compile with them.
Also, the first question's function should return bool, not int, so you can return true, not 1. The same for the other functions.
The last function can be done with only one line of code. For example:
int fib(int n){
    return n < 2 ? n : fib(n - 1) + fib(n - 2);
}