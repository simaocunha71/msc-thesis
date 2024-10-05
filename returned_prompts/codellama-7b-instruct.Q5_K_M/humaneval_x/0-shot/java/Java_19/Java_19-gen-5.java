import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String");
        String s = sc.nextLine();
        String[] arr = s.split(" ");
        Arrays.sort(arr);
        for (String i : arr) {
            System.out.print(i + " ");
        }
    }
}


