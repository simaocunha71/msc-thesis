import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    willItFly(Arrays.asList(1, 2), 5) -> false
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    willItFly(Arrays.asList(3, 2, 3), 1) -> false
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    willItFly(Arrays.asList(3, 2, 3), 9) -> true
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    willItFly(Arrays.asList(3), 5) -> true
    # 3 is less than the maximum possible weight, and it's balanced.
     */
    public boolean willItFly(List<Integer> q, int w) {
        int sum = 0;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int mid = 0;
        boolean balanced = true;
        for(int i : q){
            sum += i;
            min = Math.min(min, i);
            max = Math.max(max, i);
            mid = i;
            if(i != q.get(q.size()-1-q.indexOf(i))){
                balanced = false;
            }
        }
        if(balanced && sum <= w){
            return true;
        }else{
            return false;
        }
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced