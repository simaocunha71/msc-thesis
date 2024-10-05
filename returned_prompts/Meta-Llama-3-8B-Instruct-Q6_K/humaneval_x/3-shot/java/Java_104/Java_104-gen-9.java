        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean has_even_digit = false;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
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

