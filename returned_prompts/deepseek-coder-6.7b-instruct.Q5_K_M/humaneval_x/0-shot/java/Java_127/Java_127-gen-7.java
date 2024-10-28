    public static void main(String[] args) {
        Solution sol = new Solution();
        List<Integer> interval1 = Arrays.asList(-1, 1);
        List<Integer> interval2 = Arrays.asList(0, 4);
        System.out.println(sol.intersection(interval1, interval2));

        interval1 = Arrays.asList(-3, -1);
        interval2 = Arrays.asList(-5, 5);
        System.out.println(sol.intersection(interval1, interval2));

        interval1 = Arrays.asList(1, 2);
        interval2 = Arrays.asList(2, 3);
        System.out.println(sol.intersection(interval1, interval2));
    }
}

