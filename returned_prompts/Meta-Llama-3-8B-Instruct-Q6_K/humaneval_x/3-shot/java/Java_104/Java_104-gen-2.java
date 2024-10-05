        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
            }
            if (!hasEvenDigit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

