import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main (String[] args) throws java.lang.Exception {
        // your code goes here
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(isMultiplyPrime(n));
    }
    public static boolean isMultiplyPrime(int a) {
        // Complete this function
        if(a<100)
        return false;
        int b=a/3;
        int c=a/5;
        int d=a/7;
        return (b*c*d==a);
    }
}
