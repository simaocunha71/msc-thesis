        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean has_even_digit = false;
            while (num > 0) {
                int digit = num % 10;
                if (digit % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
                num = num / 10;
            }
            if (!has_even_digit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

