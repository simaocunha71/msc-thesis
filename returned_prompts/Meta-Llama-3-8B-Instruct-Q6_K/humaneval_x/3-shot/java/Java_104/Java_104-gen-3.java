        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            for (int digit : String.valueOf(num).chars().mapToObj(c -> String.valueOf((char) c)).collect(Collectors.toList())) {
                if (Integer.parseInt(digit) % 2 == 0) {
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

