        if(n < m) return -1;
        int sum = 0;
        for(int i = n; i <= m; i++) sum += i;
        double avg = sum/m;
        return (int)Math.round(avg);
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m).
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    roundedAvg(1, 5) => "11"
    roundedAvg(7, 5) => -1
    roundedAvg(10, 20) => "1111"
    roundedAvg(20, 33) => "11011"
     */
    public String roundedAvg(int n, int m) {

C:
        if(n > m) return "-1";
        int sum = 0;
        for(int i = n; i <= m; i++) sum += i;
        double avg = sum/m;
        return Integer.toString(Math.round(avg), 2);
    }
}

D:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m).
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    roundedAvg(1, 5) => "11"
    roundedAvg(7, 5) => -1
    roundedAvg(10, 20) => "1111"
    roundedAvg(20, 33) => "11011"
     */
    public String roundedAvg(int n, int m) {

E:
        if(n > m