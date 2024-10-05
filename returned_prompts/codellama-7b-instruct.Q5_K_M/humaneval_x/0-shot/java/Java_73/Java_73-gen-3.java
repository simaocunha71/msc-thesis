        int min = Integer.MAX_VALUE;
        for(int i = 0; i < arr.size(); i++){
            int temp = arr.get(i);
            for(int j = i + 1; j < arr.size(); j++){
                if(arr.get(j) != temp){
                    min = Math.min(min, Math.abs(arr.get(j) - temp));
                }
            }
        }
        return min;
    }
}


B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallestChange(Arrays.asList(1,2,3,5,4,7,9,6)) == 4
    smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2)) == 1
    smallestChange(Arrays.asList(1, 2, 3, 2, 1)) == 0
     */
    public int smallestChange(List<Integer> arr) {
        int min = Integer.MAX_VALUE;
        int temp;
        for(int i = 0; i < arr.size(); i++){
            for(int j = i + 1; j < arr.size(); j++){
                if(arr.get(j) != arr.get(i)){
                    temp = Math.abs(arr.get(j) - arr.get(i));
                    min = Math.min(min, temp);
                }
            }
        }
        return min;
    }
}


C:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that