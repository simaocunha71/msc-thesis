        List<Integer> result = new ArrayList<Integer>(nums);
        Collections.sort(result, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                String a_str = String.valueOf(a);
                String b_str = String.valueOf(b);
                int a_sum = 0, b_sum = 0;

                for (char c : a_str.toCharArray()) {
                    a_sum += Character.getNumericValue(c);
                }
                for (char c : b_str.toCharArray()) {
                    b_sum += Character.getNumericValue(c);
                }

                if (a_sum == b_sum) {
                    return nums.indexOf(a) - nums.indexOf(b);
                }
                return a_sum - b_sum;
            }
        });
        return result;
    }
}

