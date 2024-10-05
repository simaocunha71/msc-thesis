        int result = 0;
        for (int digit : Integer.toString(n).chars().mapToObj(c -> (char) c).map(c -> c - '0').toArray(Integer[]::new)) {
            if (digit % 2 != 0) {
                result *= digit;
            }
        }
        return result;
    }
}

