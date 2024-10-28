        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer n1, Integer n2) {
                int sum1 = 0;
                int sum2 = 0;

                String s1 = Integer.toString(n1);
                String s2 = Integer.toString(n2);

                for (int i = 0; i < s1.length(); i++) {
                    sum1 += s1.charAt(i) - '0';
                }

                for (int i = 0; i < s2.length(); i++) {
                    sum2 += s2.charAt(i) - '0';
                }

                if (sum1 == sum2) {
                    return Integer.compare(n1, n2);
                } else {
                    return Integer.compare(sum1, sum2);
                }
            }
        });
        return nums;
    }
}

