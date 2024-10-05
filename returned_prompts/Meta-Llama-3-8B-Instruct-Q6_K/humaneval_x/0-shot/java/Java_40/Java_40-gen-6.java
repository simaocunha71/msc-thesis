import java.util.*;

public class Solution {

    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<Integer>(l);
        for (int a : set) {
            Set<Integer> set2 = new HashSet<Integer>(set);
            set2.remove(a);
            for (int b : set2) {
                Set<Integer> set3 = new HashSet<Integer>(set2);
                set3.remove(b);
                if (set3.contains(-a - b)) {
                    return true;
                }
            }
        }
        return false;
    }
}
This code checks all the possible triplets of numbers in the list to see if their sum is zero. It uses a HashSet to remove duplicates and to check for existence. This way, we can check for all the possible combinations of numbers in a single pass. The time complexity is O(n^2) where n is the size of the list.

The main idea is to use a set to store the numbers in the list and then iterate over the set to find the triplets that sum up to zero. The reason for using a set here is to remove the duplicates and to check for existence in constant time. The outer loop iterates over the set, the middle loop removes the current number from the set, and the inner loop removes the current number and the previous number from the set and checks if the remaining number is present in the set. If it is, then we return true. If we don't find any such triplet, we return false. This way, we can check for all the possible combinations of numbers in a single pass. The time complexity is O(n^2) where n is the size of the list.