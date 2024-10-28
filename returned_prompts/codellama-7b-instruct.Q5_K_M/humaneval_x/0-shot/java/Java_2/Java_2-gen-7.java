import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        double number = sc.nextDouble();
        System.out.print("The number is: " + number);
        System.out.print("\nThe decimal part is: ");
        System.out.println(truncateNumber(number));
    }

    public static double truncateNumber(double number) {
        int temp = (int) number;
        return number - temp;
    }
}
