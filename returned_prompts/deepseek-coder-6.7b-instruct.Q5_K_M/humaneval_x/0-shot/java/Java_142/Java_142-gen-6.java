        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0) {
                sum += Math.pow(lst.get(i), 2);
            } else if (i % 4 == 0) {
                sum += Math.pow(lst.get(i), 3);
            } else {
                sum += lst.get(i);
            }
        }

        return sum;
    }
}

This code will loop over the list of integers, check if the index of the current integer is a multiple of 3 or 4 and perform the
appropriate operation (square or cube). If the index is not a multiple of 3 or 4, it adds the number to the sum directly. Finally, it
returns the sum.

The time complexity is O(n) where n is the size of the list. This is because it only loops over the list once. The space complexity
is O(1) as it only uses a single integer variable to keep track of the sum.

The code is correct according to the problem description, and should work as expected for all inputs.

Note: The problem statement mentions "the function shall not change the entries in the list whose indexes are not a multiple of 3 or 4".
However, the provided solution does not actually follow this requirement, as it does modify the elements based on their indices. If you
need the original list to be unchanged, you would need to create a copy of the list before performing the operations.
*/

// 2023-02-19 08:08:40.044
// 2023-02-19 08:10:04.264
// 2023-02-19 08:11:35.781
// 2023-02-19 08:13:10.202
// 2023-02-19 08:14:38.622
// 2023-02-19 08:16:10.194
//