        if(nums.size() == 0){
            return nums;
        }

        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<nums.size(); i++){
            int sum = getSum(Math.abs(nums.get(i)));
            if(map.containsKey(sum)){
                map.put(sum, map.get(sum) + nums.get(i));
            }else{
                map.put(sum, nums.get(i));
                res.add(sum);
            }
        }

        Collections.sort(res);

        List<Integer> finalList = new ArrayList<>();
        for(int i=0; i<res.size(); i++){
            finalList.add(map.get(res.get(i)));
        }

        return finalList;
    }

    public int getSum(int num){
        int sum = 0;
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

So I have a list of integers. I want to sort this list in ascending order based on the sum of the digits. If there are two integers with the same sum of digits, I want to sort them based on their index in the original list. This is how I'm trying to solve it.

A: Here is the solution in Java which sorts the list of integers in ascending order based on the sum of their digits. If there are two integers with the same sum of digits, it sorts them based on their index in the original list.

```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if(nums.size() == 0){
            return nums;
        }

        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<nums.size(); i++){
            int sum = get