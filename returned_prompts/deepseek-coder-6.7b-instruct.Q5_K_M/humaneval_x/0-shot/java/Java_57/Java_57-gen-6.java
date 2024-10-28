        if(l.size() == 0 || l.size() == 1)
            return true;

        int i = 0;
        while(i < l.size()-1 && l.get(i) == l.get(i+1)) {
            i++;
        }

        if(i == l.size()-1)
            return true;

        boolean increasing = l.get(i) < l.get(i+1);

        while(i < l.size()-1) {
            if(increasing && l.get(i) > l.get(i+1))
                return false;
            if(!increasing && l.get(i) < l.get(i+1))
                return false;
            i++;
        }

        return true;
    }
}

The solution uses a while loop to skip the identical elements at the beginning of the list. Then it sets the 'increasing' variable according to whether the first two different elements are increasing or decreasing. It then checks the remaining elements of the list to ensure they follow the same pattern as the first two elements.

If any element breaks the pattern, it returns false. If it gets through the whole list without finding a break in the pattern, it returns true.
*/

//Test cases
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.monotonic(Arrays.asList(1, 2, 4, 20))); //true
        System.out.println(sol.monotonic(Arrays.asList(1, 20, 4, 10))); //false
        System.out.println(sol.monotonic(Arrays.asList(4, 1, 0, -10))); //true
    }
}

//Output:
//true
//false
//true

//This is the most optimal solution to this problem in terms of time complexity. It has a time complexity of O(n) because it goes through the list only once.

//The space complexity is also O(n) because of the space required for the list.

//If the space complexity is a concern