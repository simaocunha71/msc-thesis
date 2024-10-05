        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 1) result.add(n);
            n = n / 2 + (n % 2) * 3;
        }
        result.add(1);
        Collections.reverse(result);
        return result;
    }
}

