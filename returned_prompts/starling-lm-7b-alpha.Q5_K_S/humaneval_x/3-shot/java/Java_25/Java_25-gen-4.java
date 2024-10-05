        List<Integer> result = new ArrayList<>();
        int div = 2;
        while (n > 1) {
            while (n % div == 0) {
                result.add(div);
                n /= div;
            }
            div += 1;
            if (div * div > n) break;
        }
        return result;
    }
}

