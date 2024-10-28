        List<Integer> sortedList = new ArrayList<>(nums);
        Collections.sort(sortedList, (a, b) -> {
            int sumA = 0, sumB = 0;
            for (char c : String.valueOf(a).toCharArray()) {
                sumA += Character.getNumericValue(c);
            }
            for (char c : String.valueOf(b).toCharArray()) {
                sumB += Character.getNumericValue(c);
            }
            if (sumA == sumB) {
                return Integer.compare(nums.indexOf(a), nums.indexOf(b));
            } else {
                return Integer.compare(sumA, sumB);
            }
        });
        return sortedList;
    }
}

