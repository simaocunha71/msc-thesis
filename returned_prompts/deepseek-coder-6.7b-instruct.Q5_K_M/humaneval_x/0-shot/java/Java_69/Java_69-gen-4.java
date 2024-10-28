        Collections.sort(lst);
        int max = -1;
        int count = 1;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i).equals(lst.get(i - 1))) {
                count++;
                if (count >= lst.get(i)) {
                    max = Math.max(max, lst.get(i));
                }
            } else {
                count = 1;
            }
        }
        return max;
    }
}

Explanation:
Here, we're sorting the given list and then traversing it. We're maintaining two variables, max and count. Max is used to store the greatest integer that has a frequency greater than or equal to the value of the integer itself. Count is used to track the frequency of the current number. If at any point the count is greater than or equal to the current number, we update the max. If we traverse the entire list and still no such number exists, we return -1.

This solution works because it sorts the list, which allows for easy comparison of successive numbers. It then counts the frequency of each number and checks if it is greater than or equal to the number itself. If it is, it updates the max. Finally, it returns the max. If no such number exists, it returns -1.
*/


/*
