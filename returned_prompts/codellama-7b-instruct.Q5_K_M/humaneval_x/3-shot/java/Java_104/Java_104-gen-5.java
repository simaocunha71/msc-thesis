        List<Integer> result = new ArrayList<>();
        Set<Integer> seen = new HashSet<>();

        for (int i : x) {
            if (i == 0) continue;

            while (i > 0) {
                int digit = i % 10;
                if (digit % 2 == 0) {
                    seen.add(digit);
                    break;
                }
                i /= 10;
            }
        }

        for (int i : seen) {
            result.add(i);
        }

        Collections.sort(result);
        return result;
    }
}

