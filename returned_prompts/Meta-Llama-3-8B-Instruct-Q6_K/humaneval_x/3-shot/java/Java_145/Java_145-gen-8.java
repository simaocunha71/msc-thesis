        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>(nums);
        temp.sort((a, b) -> {
            int sumA = 0, sumB = 0;
            for (char c : String.valueOf(a).toCharArray()) {
                sumA += Character.getNumericValue(c);
            }
            for (char c : String.valueOf(b).toCharArray()) {
                sumB += Character.getNumericValue(c);
            }
            if (sumA != sumB) {
                return sumA - sumB;
            } else {
                return Integer.compare(temp.indexOf(a), temp.indexOf(b));
            }
        });
        return temp;
    }
}