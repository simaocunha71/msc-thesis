        List<Integer> result = new ArrayList<>();
        int current = n;
        while (n > 0) {
            result.add(current);
            n--;
            if (n % 2 == 1) {
                current += 2;
            } else {
                current += 1;
            }
        }
        Collections.reverse(result);
        return result;
    }
}

