        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            if (hasNoEvenDigits(i)) {
                result.add(i);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasNoEvenDigits(int i) {
        while (i > 0) {
            int d = i % 10;
            if (d % 2 == 0) return false;
            i /= 10;
        }
        return true;
    }
}


