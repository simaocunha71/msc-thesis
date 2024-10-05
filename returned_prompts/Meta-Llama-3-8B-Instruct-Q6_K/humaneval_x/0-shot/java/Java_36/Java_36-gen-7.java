        int count = 0;
        for (int i = 11; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = String.valueOf(i);
                count += Collections.frequency(Arrays.asList(s.split ""), "7");
            }
        }
        for (int i = 7; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += Collections.frequency(Arrays.asList(String.valueOf(i).split ""), "7");
            }
        }
        return count;
    }
}
