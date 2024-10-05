public class Solution {
    public Object roundedAvg(int n, int m) {
        if(n > m) {
            return -1;
        }
        int sum = 0;
        for(int i = n; i <= m; i++) {
            sum += i;
        }
        double avg = (double) sum / (m - n + 1);
        avg = Math.round(avg);
        String binary = Integer.toBinaryString((int) avg);
        return binary;
    }
}
The code calculates the sum of the integers from n to m, calculates the average by dividing the sum by the number of integers, rounds the average to the nearest integer using the Math.round() method, and then converts the rounded average to binary using the Integer.toBinaryString() method. If n is greater than m, the code returns -1. The result is a binary string representation of the rounded average. 
Note that the problem statement is slightly unclear, but the code assumes that the average should be rounded to the nearest integer, not rounded to the nearest decimal. If the problem intended the average to be rounded to the nearest decimal, the code would need to be modified accordingly. 