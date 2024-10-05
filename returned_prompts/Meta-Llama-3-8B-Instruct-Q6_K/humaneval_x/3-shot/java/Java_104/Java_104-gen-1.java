        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Character.getNumericValue(c) % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
            }
            if (!hasEvenDigit) result.add(num);
        }
        result.sort((a, b) -> Integer.compare(a, b));
        return result;
    }
}

