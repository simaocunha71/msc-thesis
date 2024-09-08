    int count = 0; // Initialize count of changes
    int left = 0;   // Initialize left pointer
    int right = arr.size() - 1; // Initialize right pointer

    while (left < right) {
        if (arr[left] == arr[right]) {
            left++; // Move left pointer
            right--; // Move right pointer
        } else {
            if (arr[left + 1] == arr[right]) {
                arr[left] = arr[left + 1]; // Change left element
                left++; // Move left pointer
                right--; // Move right pointer
            } else if (arr[left] == arr[right - 1]) {
                arr[right] = arr[left]; // Change right element
                left++; // Move left pointer
                right--; // Move right pointer
            } else {
                left++; // Move left pointer
                right--; // Move right pointer
                count++; // Increment count of changes
            }
        }
    }
    return count; // Return count of changes
}

