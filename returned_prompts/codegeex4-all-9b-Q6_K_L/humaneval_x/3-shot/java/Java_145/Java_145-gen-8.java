        Collections.sort(nums, (a, b) -> {
            int a_sum = 0, b_sum = 0;
            for (char c : String.valueOf(a).toCharArray()) {
                a_sum += Character.getNumericValue(c);
            }
            for (char c : String.valueOf(b).toCharArray()) {
                b_sum += Character.getNumericValue(c);
            }
            return Integer.compare(a_sum, b_sum);
        });
        return nums;

    }
}

