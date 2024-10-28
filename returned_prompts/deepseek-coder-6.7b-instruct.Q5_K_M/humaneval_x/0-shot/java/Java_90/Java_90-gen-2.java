        if(lst.size() < 2)
            return Optional.empty();

        int smallest = Integer.MAX_VALUE;
        int second_smallest = Integer.MAX_VALUE;

        for(int num : lst){
            if(num < smallest){
                second_smallest = smallest;
                smallest = num;
            }
            else if(num > smallest && num < second_smallest){
                second_smallest = num;
            }
        }

        if(second_smallest == Integer.MAX_VALUE)
            return Optional.empty();

        return Optional.of(second_smallest);
    }
}

Explanation:
This problem is asking for the 2nd smallest number in the list. We can use two variables smallest and second_smallest to track the smallest and 2nd smallest numbers. We then iterate through the list and update smallest and second_smallest accordingly.

If the second_smallest remains as the initial value at the end of the list (which means no 2nd smallest number exists), we return Optional.empty(). Otherwise, we return Optional.of(second_smallest) which gives us the 2nd smallest number.

Note:
This solution assumes that the list contains unique integers. If the list can contain duplicates, we should not update second_smallest if it is equal to smallest.

Also, the size of the list can be at most 10^5. So, the time complexity of the solution is O(n).

This solution should work in Java 8 and above.
*/

//End of code

//End of Solution

//End of Code

//End of Solution

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

