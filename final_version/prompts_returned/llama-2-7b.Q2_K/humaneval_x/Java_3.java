import java.util.*;
import java.lang.*;

class Solution {
    /**
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> belowZero(Arrays.asList(1, 2, 3))
    false
    >>> belowZero(Arrays.asList(1, 2, -4, 5))
    true
     */
    public boolean belowZero(List<Integer> operations) {
        int currentBalance = 0;
        for (int i = 0 ; i < operations.size() ; i++) {
            if(operations.get(i) == -1 ){
                currentBalance += operations.get(-1);
            }else{
                currentBalance -= operations.get(i);
            }
        }
        return (currentBalance < 0 ? true : false);
    }
}