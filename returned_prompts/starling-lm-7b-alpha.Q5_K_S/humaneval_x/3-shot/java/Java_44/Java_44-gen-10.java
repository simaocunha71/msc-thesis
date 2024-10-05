        List<Integer> remainders = new ArrayList<>();
        while (x > 0) {
            int remainder = x % base;
            x = x / base;
            remainders.add(remainder);
        }
        StringBuilder result = new StringBuilder();
        for (int i = remainders.size() - 1; i >= 0; i--) {
            result.append(remainders.get(i));
        }
        return result.toString();
    }
}

