        List<Integer> result = new ArrayList<>();
        for (int value : x) {
            if (value % 2 == 0) continue;
            int last = value;
            while (last > 0) {
                int digit = last % 10;
                if (digit % 2 == 0) {
                    break;
                }
                last /= 10;
            }
            if (last == 0) {
                result.add(value);
            }
        }
        Collections.sort(result);
        return result;
    }
}

