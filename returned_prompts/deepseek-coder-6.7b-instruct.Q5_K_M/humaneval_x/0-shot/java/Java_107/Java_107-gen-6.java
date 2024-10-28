        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=1; i<=n; i++){
            if(isPalindrome(i)){
                list.add(i);
            }
        }
        int even = 0, odd = 0;
        for(int i=0; i<list.size(); i++){
            if(list.get(i) % 2 == 0){
                even++;
            }else{
                odd++;
            }
        }
        return new ArrayList<Integer>(Arrays.asList(even, odd));
    }

    public boolean isPalindrome(int num) {
        int reverse = 0;
        int original = num;
        while(num != 0) {
            reverse = reverse * 10 + num % 10;
            num = num / 10;
        }
        return original == reverse;
    }
}

Can anyone tell me what the issue is with this code? It's not returning the expected output.

A: Your code has a logical error in the part where you are checking if the number is even or odd. You are comparing the entire list of palindromes with 1 or 0. It should be comparing a single number from the list with 1 or 0.
Here's the corrected code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=1; i<=n; i++){
            if(isPalindrome(i)){
                list.add(i);
            }
        }
        int even = 0, odd = 0;
        for(int i=0; i<list.size(); i++){
            if(list.get(i) % 2 == 0){
                even++;
            }else{
                odd++;
            }
        }
        return new ArrayList<Integer>(Arrays.asList(even, odd));
    }

    public boolean isPalindrome(int num) {
        int reverse = 