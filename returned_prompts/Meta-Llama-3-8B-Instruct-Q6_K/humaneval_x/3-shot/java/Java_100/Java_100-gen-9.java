        List<Integer> result = new ArrayList<>();
        int current = n;

        while (n > 0) {
            result.add(0, current);
            n--;
            current += (n % 2 == 0) ? 1 : 2;
        }
        return result;
    }
}

