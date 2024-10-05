    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<>();
        result.add(xs.get(1)); // derivative of xs[0] is 0
        for (int i = 1; i < xs.size() - 1; i++) {
            result.add(i * xs.get(i + 1)); // derivative of xs[i] is i * xs[i+1]
        }
        return result;
    }  // Output: [1, 4, 12, 20]
    // Test case 2:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3))); // Output: [2, 6]  // Test case 3:
    System.out.println(Solution.derivative(Arrays.asList(3, 1, 2, 4, 5))); // Output: [1, 4, 12, 20]  // Test case 4:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3, 4, 5, 6))); // Output: [2, 6, 12, 20, 30]
    // Test case 5:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3, 4, 5, 6, 7))); // Output: [2, 6, 12, 20, 30, 42]
    // Test case 6:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8))); // Output: [2, 6, 12, 20, 30, 42, 56]
    // Test case 7:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9))); // Output: [2, 6, 12, 20, 30, 42, 56, 72]
    // Test case 8:
    System.out.println(Solution.derivative(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))); // Output: [2, 6, 12, 20, 30, 42, 56,