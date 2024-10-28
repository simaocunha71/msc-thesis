    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int countA = Integer.toBinaryString(a).replaceAll("0", "").length();
                int countB = Integer.toBinaryString(b).replaceAll("0", "").length();
                if (countA == countB) {
                    return a.compareTo(b);
                } else {
                    return countA - countB;
                }
            }
        });
        return arr;
    }  // This solution uses Java's built-in sort function and a custom comparator to sort the array based on the number of ones in the binary representation of each integer.
    The comparator first counts the number of ones in the binary representation of each integer, and then compares the integers based on this count. If two integers have the same count of ones, it compares them based on their decimal value. The sorted array is then returned.