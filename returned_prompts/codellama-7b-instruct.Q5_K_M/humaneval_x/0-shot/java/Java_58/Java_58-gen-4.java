        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < l1.size(); i++) {
            for (int j = 0; j < l2.size(); j++) {
                if (l1.get(i).equals(l2.get(j))) {
                    result.add(l1.get(i));
                    break A;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().common(Arrays.asList(1, 4, 3, 34, 653, 2, 5), Arrays.asList(5, 7, 1, 5, 9, 653, 121)));
        System.out.println(new Solution().common(Arrays.asList(5, 3, 2, 8), Arrays.asList(3, 2)));
    }
}
