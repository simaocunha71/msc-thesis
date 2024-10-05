import java.util.*;
import java.lang.*;

class Solution {
    /**
    Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
     */
    public List<Integer> f(int n) {
        List<Integer> result = new ArrayList<Integer>();
        for(int i = 1; i <= n; i++){
            if(i % 2 == 0){
                result.add(f(i));
            } else {
                result.add(sum(i));
            }
        }
        return result;
    }
    public int f(int i){
        int result = 1;
        for(int j = 2; j <= i; j++){
            result *= j;
        }
        return result;
    }
    public int sum(int n){
        int result = 0;
        for(int i = 1; i <= n; i++){
            result += i;
        }
        return result;
    }
}

