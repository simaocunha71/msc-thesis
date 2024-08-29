/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        System.out.println(fib(10));
        System.out.println(fib(1));
        System.out.println(fib(8));
    }
    public static int fib(int n) {
        if(n<=1) return n;
        return fib(n-1)+fib(n-2);
    }
}

B:
/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
#include<stdio.h>
using namespace std;
int fib(int n){
    if(n<=1) return n;
    return fib(n-1)+fib(n-2);
}

C:
/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        System.out.println(fib(10));
        System.out.println(fib(1));
        System.out.println(fib(8));
    }
    public static int fib(int n) {
        int a = 0;
        int b = 1;
        if(n<=1) return n;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}

D:
/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        System.out.println(fib(10));
        System.out.println(fib(1));
        System.out.println(fib(8));
    }
    public static int fib(int n) {
        int a = 0;
        int b = 1;
        if(n<=1) return n;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
}
E:
/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
