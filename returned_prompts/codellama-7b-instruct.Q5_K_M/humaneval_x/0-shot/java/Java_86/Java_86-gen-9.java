import java.util.*;
import java.lang.*;

class Solution {
    public int[] getSortedArray(int arr[], int n) {
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = arr[i];
        }
        Arrays.sort(result);
        return result;
    }

    public int[] getSortedArray(int[] arr, int start, int end) {
        int[] result = new int[end - start + 1];
        for (int i = start; i <= end; i++) {
            result[i - start] = arr[i];
        }
        Arrays.sort(result);
        return result;
    }

    public int[] getUniqueArray(int[] arr, int n) {
        int[] result = new int[n];
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] != arr[j]) {
                result[j] = arr[i];
                j++;
            }
        }
        return result;
    }

    public int[] getUniqueArray(int[] arr, int start, int end) {
        int[] result = new int[end - start + 1];
        int j = 0;
        for (int i = start; i <= end; i++) {
            if (arr[i] != arr[j]) {
                result[j] = arr[i];
                j++;
            }
        }
        return result;
    }

    public int[] getUniqueArray(int[] arr) {
        return getUniqueArray(arr, 0, arr.length - 1);
    }
}
