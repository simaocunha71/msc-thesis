        List<Integer> result = new ArrayList<Integer>();
        List<Integer> third = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                third.add(l.get(i));
            } else {
                result.add(l.get(i));
            }
        }
        result.addAll(third);
        Collections.sort(result);
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sortThird(Arrays.asList(1, 2, 3)));
        System.out.println(solution.sortThird(Arrays.asList(5, 6, 3, 4, 8, 9, 2)));
    }
}


