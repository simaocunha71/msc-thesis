        List<Integer> result = new ArrayList<>();
        while (n > 0) {
            result.add(n % 10);
            n /= 10;
        }
        Collections.reverse(result);
        return result;
    }
}

