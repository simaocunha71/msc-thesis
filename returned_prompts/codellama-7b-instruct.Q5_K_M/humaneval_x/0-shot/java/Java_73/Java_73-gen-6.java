        // Sort the list and find the minimum difference between the first and last elements
        // of the list. The difference is the number of elements that need to be changed
        // to make the list palindromic.
        int minDiff = Integer.MAX_VALUE;
        Collections.sort(arr);
        int first = arr.get(0);
        int last = arr.get(arr.size() - 1);
        minDiff = last - first;
        if (minDiff < 0) {
            minDiff = -minDiff;
        }
        return minDiff;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println("smallestChange(Arrays.asList(1,2,3,5,4,7,9,6)) == 4: " + sol.smallestChange(Arrays.asList(1,2,3,5,4,7,9,6)));
        System.out.println("smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2)) == 1: " + sol.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2)));
        System.out.println("smallestChange(Arrays.asList(1, 2, 3, 2, 1)) == 0: " + sol.smallestChange(Arrays.asList(1, 2, 3, 2, 1)));
    }
}
