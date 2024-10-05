    public int smallestChange(List<Integer> arr) {
        // Convert the list to an array
        int[] arrArray = arr.stream().mapToInt(i -> i).toArray();

        // Initialize variables to store the minimum number of changes
        int left = 0, right = arrArray.length - 1;
        int minChanges = 0;

        // Compare elements from the start and end, move towards the center
        while (left < right) {
            if (arrArray[left] != arrArray[right]) {
                // If elements are not equal, increment the changes and move towards the center
                minChanges++;
                // Move the pointer closest to the center
                if (left + 1 < right) {
                    left++;
                } else {
                    right--;
                }
            } else {
                // If elements are equal, move towards the center
                left++;
                right--;
            }
        }

        // Return the minimum number of changes
        return minChanges;
    }
}