class Solution {
    /**
    Return sorted unique common elements for two lists.
    >>> common(Arrays.asList(1, 4, 3, 34, 653, 2, 5), Arrays.asList(5, 7, 1, 5, 9, 653, 121))
    [1, 5, 653]
    >>> common(Arrays.asList(5, 3, 2, 8), Arrays.asList(3, 2))
    [2, 3]
     */
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {

        for (Integer n1 : l1) {
            for (Integer n2 : l2) {
                if (n1.equals(n2)) {
                    continue A;
                }
            }
            l2.add(n1);
        }

        Collections.sort(l2);
        return l2;
    }
}
