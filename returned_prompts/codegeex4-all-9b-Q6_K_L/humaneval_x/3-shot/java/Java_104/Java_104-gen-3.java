        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            boolean has_even = false;
            while (i > 0) {
                int digit = i % 10;
                if (digit % 2 == 0) {
                    has_even = true;
                    break;
                }
                i /= 10;
            }
            if (!has_even) result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

