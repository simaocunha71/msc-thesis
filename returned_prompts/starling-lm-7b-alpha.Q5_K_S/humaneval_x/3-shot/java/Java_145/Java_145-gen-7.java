        List<Integer> result = new ArrayList<>();

        Collections.sort(nums, (a, b) -> {
            int a_sum = Math.abs(Integer.parseInt(String.valueOf(Math.abs(a)))) + Math.abs(a);
            int b_sum = Math.abs(Integer.parseInt(String.valueOf(Math.abs(b)))) + Math.abs(b);

            if (a_sum != b_sum) return Integer.compare(a_sum, b_sum);
            return Integer.compare(a, b);
        });

        return result;
    }
}

