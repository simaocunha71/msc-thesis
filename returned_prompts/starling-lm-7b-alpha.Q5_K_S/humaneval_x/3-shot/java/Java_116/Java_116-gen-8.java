        Collections.sort(arr, (a, b) -> {
            int a_count = 0;
            int b_count = 0;
            while (a > 0) {
                a_count += 1;
                a = a / 2;
            }
            while (b > 0) {
                b_count += 1;
                b = b / 2;
            }
            return a_count == b_count ? Integer.compare(a, b) : Integer.compare(a_count, b_count);
        });
        return arr;
    }
}

