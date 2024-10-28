        int count = 0;
        for (int i = 1; i <= n; i++) {
            String number = Integer.toString(i);
            if (number.startsWith("1") || number.endsWith("1")) {
                count += 1;
            }
        }
        return count;
    }
}

