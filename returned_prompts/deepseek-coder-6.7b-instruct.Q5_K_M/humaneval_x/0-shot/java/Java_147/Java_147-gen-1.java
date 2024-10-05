        int count = 0;
        int[] arr = new int[n+1];
        for(int i = 1; i <= n; i++) {
            arr[i] = (i * i) - i + 1;
        }
        for(int i = 1; i <= n-2; i++) {
            for(int j = i+1; j <= n-1; j++) {
                for(int k = j+1; k <= n; k++) {
                    if((arr[i] + arr[j] + arr[k]) % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}

This problem is asking to create an array of n elements where each element is calculated by the formula (i * i) - i + 1. Then it is asked to find the number of triplets in the array where each element is a multiple of 3.
This solution is a brute force approach where it checks all possible triplets and increments a counter whenever a valid triplet is found.
The time complexity of this solution is O(n^3) and the space complexity is O(n), where n is the length of the array.
*/

//Test Cases
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 5;
        int result = sol.getMaxTriples(n);
        System.out.println(result); //Expected output: 1

        n = 3;
        result = sol.getMaxTriples(n);
        System.out.println(result); //Expected output: 0
    }
}
/*
Test Case 1:
Input: n = 5
Output: 1
Explanation:
a = [1, 3, 7, 13, 21]
The only valid triple is (1, 7, 13).

Test Case 2:
Input: n = 3
Output: 0
Explanation:
a = [1, 3, 7]
There are no valid triplets.
*/

//Notes: 
/*
This solution