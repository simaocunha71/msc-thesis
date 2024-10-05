        for (int i = 0; i < 10000; ++i) {
            int c = i * i * i;
            if (c == a) {
                return true;
            }
        }
        return false;
    }

    /**
    Write a function that takes two integer arrays a and b of length n.
    The function should return the minimum number of swaps required to sort the elements in array a to be the same as the order in array b.
    Note: you may assume the input is always valid.
    Examples:
    minSwaps(new int[]{3, 2, 1}, new int[]{1, 2, 3}) ==> 0
    minSwaps(new int[]{1, 3, 2}, new int[]{2, 1, 3}) ==> 1
    minSwaps(new int[]{2, 1, 3}, new int[]{3, 2, 1}) ==> 2
    minSwaps(new int[]{1, 3, 2}, new int[]{3, 2, 1}) ==> 1
    minSwaps(new int[]{2, 1, 4}, new int[]{3, 2, 1}) ==> 2
    minSwaps(new int[]{2, 1, 3}, new int[]{1, 2, 3}) ==> 0
     */
    public int minSwaps(int[] a, int[] b) {
        int[] pos = new int[10000];
        for (int i = 0; i < a.length; ++i) {
            pos[a[i]] = i;
        }

        int res = 0;
        int at = 0;
        for (int i = 0; i < a.length; ++i) {
            int cur = b[i];
            if (pos[cur] < at) {
                ++res;
                at = pos[cur];
            } else {
                at = pos[cur] + 1;
            }
        }
        return res;
    }
}


















