        List<Integer> result = new ArrayList<>();
        Collections.sort(arr, (a, b) -> {
            int countA = Integer.bitCount(a);
            int countB = Integer.bitCount(b);
            if (countA == countB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(countA, countB);
            }
        });
        return result;
    }
}

