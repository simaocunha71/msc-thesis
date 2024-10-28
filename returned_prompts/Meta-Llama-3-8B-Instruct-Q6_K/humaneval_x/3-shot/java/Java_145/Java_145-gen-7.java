        List<Integer> result = new ArrayList<>();
        nums.sort((a, b) -> {
            int sumA = 0, sumB = 0;
            for (char c : Integer.toString(a).toCharArray()) {
                sumA += Integer.parseInt(String.valueOf(c));
            }
            for (char c : Integer.toString(b).toCharArray()) {
                sumB += Integer.parseInt(String.valueOf(c));
            }
            if (sumA == sumB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(sumA, sumB);
            }
        });
        return result;
    }
}

