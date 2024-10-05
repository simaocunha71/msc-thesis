        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            String num_string = String.valueOf(num);
            boolean has_even_digit = false;
            for (char c : num_string.toCharArray()) {
                int digit = Character.getNumericValue(c);
                if (digit % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
            }
            if (!has_even_digit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

