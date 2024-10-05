        // Sort the input list
        Collections.sort(arr);

        // Find the maximum value
        int max = arr.get(k - 1);

        // Find the sum of the first k elements
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += arr.get(i);
        }

        // Find the minimum value
        int min = arr.get(0);

        // Find the sum of the last k elements
        int sum2 = 0;
        for (int i = k - 1; i < arr.size(); i++) {
            sum2 += arr.get(i);
        }

        return (max - min) + (sum - sum2);
    }
}


// 1. Sort the input list
// 2. Find the maximum value
// 3. Find the sum of the first k elements
// 4. Find the minimum value
// 5. Find the sum of the last k elements
// 6. Return (max - min) + (sum - sum2)


// 7. Find the sum of the first k elements
// 8. Find the sum of the last k elements
// 9. Return (max - min) + (sum - sum2)
