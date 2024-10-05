        List<Integer> result = new ArrayList<>();
        if(numbers.size() == 0) return result;
        
        int max = numbers.get(0);
        result.add(max);
        
        for(int i = 1; i < numbers.size(); i++){
            if(numbers.get(i) > max){
                max = numbers.get(i);
            }
            result.add(max);
        }
        return result;
    }
}

Explanation:
The program creates a new list to store the result. If the input list is empty, it returns an empty list right away. Otherwise, it sets the first number as the maximum and adds it to the result list.
It then loops over the rest of the list, updating the maximum whenever it finds a larger number and adding the new maximum to the result list.
Finally, it returns the result list.

The time complexity of this program is O(n), where n is the length of the list. This is because the program performs a constant amount of work for each element in the list. The space complexity is also O(n) because the program uses a list to store the result.

This program assumes that the input list is not null and does not contain null elements.

This solution is correct according to the problem statement.

I hope this helps you understand the solution. Let me know if you have any more questions.

*/

public class Main
{
    public static void main(String[] args)
    {
        Solution sol = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 3, 4, 2);
        System.out.println(sol.rollingMax(numbers));
    }
}


// Output: [1, 2, 3, 3, 3, 4, 4]














































































