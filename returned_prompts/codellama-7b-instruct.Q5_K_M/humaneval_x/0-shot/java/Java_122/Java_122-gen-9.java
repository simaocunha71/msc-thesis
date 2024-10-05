        int sum = 0;
        int length = arr.size();
        int count = 0;
        for (int i = 0; i < length; i++) {
            int num = arr.get(i);
            if (num < 10) {
                sum += num;
                count++;
            } else if (num < 100) {
                sum += num - num % 10;
                count++;
            }
            if (count == k) {
                break;
            }
        }
        return sum;
    }

    /**
    Given an array of integers arr, and three integers a, b, and c. You need to find the number of
    different kind of triplets could you make using the elements of the array arr.

    Example 1:

        Input: arr = [1,2,1,2,3,1], a = 2, b = 3, c = 2
        Output: 2
        Explanation: The two triplets are: [1,2,1] and [2,3,1].

    Example 2:

        Input: arr = [1,1,1,1,1], a = 1, b = 1, c = 1
        Output: 5
        Explanation: The five triplets are: [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1].

    Example 3:

        Input: arr = [7,7,7,7,7], a = 7, b = 7, c = 7
        Output: 1
        Explanation: The only triplet is [7,7,7].

    Example 4:

        Input: arr = [4, 4, 4, 4], a = 4, b = 4, c = 4
        Output: 1

    Constraints:
        1. 3 <= len(arr) <= 3000
        2. 1 <= arr[i] <= 1000
        3. 1 <= a, b, c <= 1