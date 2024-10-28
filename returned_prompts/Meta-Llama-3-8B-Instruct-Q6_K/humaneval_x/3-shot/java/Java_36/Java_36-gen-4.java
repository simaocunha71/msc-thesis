        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String str = String.valueOf(i);
                count += Collections.frequency(Arrays.asList(str.split ""), "7");
            }
        }
        return count;
    }
}

