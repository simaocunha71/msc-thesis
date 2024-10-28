    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> numSet = new HashSet<Integer>(l);
        for (int num : numSet) {
            if (numSet.contains(-num) && numSet.contains(num * 2)) {
                return true;
            }
        }
        return false;
    }
    
    // Test cases:
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.triplesSumToZero(Arrays.asList(1, 3, 5, 0))); // false
        System.out.println(solution.triplesSumToZero(Arrays.asList(1, 3, -2, 1))); // true
        System.out.println(solution.triplesSumToZero(Arrays.asList(1, 2, 3, 7))); // false
        System.out.println(solution.triplesSumToZero(Arrays.asList(2, 4, -5, 3, 9, 7))); // true
        System.out.println(solution.triplesSumToZero(Arrays.asList(1))); // false
    }
    
    // Convert list to set
    public static List<Integer> Arrays.asList(Object... objects) {
        return new ArrayList<Integer>(Arrays.asList(objects));
    }
    
    // Convert set back to list
    public static List<Integer> setToList(Set<Integer> set) {
        return new ArrayList<Integer>(set);
    }
    
    // Convert list to array
    public static Object[] listToArray(List<Integer> list) {
        return list.toArray();
    }
    // Convert array to list
    public static List<Integer> arrayToList(Object[] array) {
        return new ArrayList<Integer>(Arrays.asList(array));
    }
    
    // Convert list to set
    public static Set<Integer> setOf(List<Integer> list) {
        return new HashSet<Integer>(list);
    }
    
    // Convert set to list
    public static List<Integer> listFromSet(Set<Integer> set) {
        return new ArrayList<Integer>(set);
    }
    
    // Convert array to set
    public static Set<Integer> setOfArray(Object[] array) {
        return new HashSet<Integer>(Arrays.asList(array));
    }
    
    // Convert set to array
    public static Object[] arrayFromSet(Set<Integer> set) {
        return set.toArray();
    }    
    // Convert array to list
    public static List<Integer> listFromArray(Object[] array) {
        return new ArrayList<Integer>(Arrays.asList(array));
   