        if(n <= 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        int a = 0, b = 1, result = 0;
        for(int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
}
B:
import java.util.*;
import java.lang.*;

class Solution {
    public int fib(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}
C:
import java.util.*;
import java.lang.*;

class Solution {
    public int fib(int n) {
        if(n <= 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        int a = 0, b = 1, result = 0;
        for(int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
}
D:
public class Solution {
    public int fib(int n) {
        if(n <= 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        int a = 0, b = 1, result = 0;
        for(int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
}
E:
public class Solution {
    public int fib(int n) {
        if(n <= 0) {
            return 0;
        } else if(n == 1) {
            return 1;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}F:
public class Solution {
    public int fib(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}
G:
public class