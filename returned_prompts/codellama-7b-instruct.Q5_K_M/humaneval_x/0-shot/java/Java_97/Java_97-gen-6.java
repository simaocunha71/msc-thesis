import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=multiply(a,b);
        System.out.println(c);
    }
    public static int multiply(int a, int b) {
        int x=a%10;
        int y=b%10;
        int z=x*y;
        return z;
    }
}
