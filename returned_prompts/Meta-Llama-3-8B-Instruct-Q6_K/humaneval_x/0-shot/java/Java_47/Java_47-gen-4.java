    public double median(List<Integer> l) {
        // Create a copy of the list
        List<Integer> list = new ArrayList<>(l);
        // Sort the list
        Collections.sort(list);
        // Calculate the length of the list
        int n = list.size();
        // If the length of the list is odd
        if (n % 2 == 1) {
            // Return the middle element
            return (double) list.get(n / 2);
        } else {
            // Calculate the median
            int mid1 = list.get(n / 2 - 1);
            int mid2 = list.get(n / 2);
            return (double) (mid1 + mid2) / 2;
        }
    }