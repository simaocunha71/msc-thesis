        List<Integer> result = new ArrayList<>();
        int even_count = 0;
        int odd_count = 0;

        for (char c : String.valueOf(num).toCharArray()) {
            if (Character.isDigit(c)) {
                int digit = Integer.parseInt(String.valueOf(c));
                if (digit % 2 == 0) {
                    even_count++;
                } else {
                    odd_count++;
                }
            }
        }
        result.add(even_count);
        result.add(odd_count);
        return result;
    }
}

