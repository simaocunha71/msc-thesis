        List<Integer> oddCollatz = new ArrayList<>();
        while (n != 1) {
            oddCollatz.add(n);
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
        }
        oddCollatz.add(n);

        return oddCollatz;
    }
}


