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
    public Object roundedAvg(int n, int m) {
        // TODO: Implement this method.
        String[] res=new StringBuilder().append(n).append("").toString();
        for(int i=1;i<m+1;i++){
            res = new StringBuilder().append(res).append((char)(48+(n%i))).append(",").toString(); 
        }
        return res.substring(0, res.length()-1);   
        
        //return "1";
    }
}

public class Solution2 {
	/**
     * 输入: n = 987654321, m = 33
     * 输出: "1001"
     */
    public Object roundedAvg(int n, int m) {
        // TODO: Implement this method.
        String[] res=new StringBuilder().append(n).append("").toString();
        for(int i=1;i<m+1;i++){
            res = new StringBuilder().append((char)(65+(n%i))).append(",").toString(); 
        }
        return res.substring(0, res.length()-1);   
    }
}