        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            String s = Integer.toString(i);
            for (int j = 0; j < s.length(); j++) {
                int digit = s.charAt(j) - '0';
                if (digit % 2 == 0) {
                    result.add(digit);
                }
            }
        }
        Collections.sort(result);
        return result;
    }
}

