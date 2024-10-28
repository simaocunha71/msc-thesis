        for(int i = 0; i < lst.size()-1; i++){
            if(lst.get(i) >= lst.get(i+1)) {
                return false;
            }
        }
        return true;
    }
}

This code will return false if the current number is equal to or greater than the next number in the list. If none of the numbers in the list meet this condition, the method will return true, indicating that the list is sorted in ascending order.

The time complexity of this solution is O(n), where n is the length of the list. This is because we iterate through the list once. The space complexity is O(1), because we only use a constant amount of space to store the indices and the list itself.

This solution assumes that the list has no negative numbers and only integers, as stated in the problem description. If this is not the case, the solution would need to be adjusted accordingly.
 */

// 