        boolean is_increasing = true;
        boolean is_decreasing = true;

        for (int i = 0; i < l.size() - 1; i++) {
            int a = l.get(i);
            int b = l.get(i + 1);

            if (a > b) {
                is_increasing = false;
            }
            if (a < b) {
                is_decreasing = false;
            }
        }
        return is_increasing || is_decreasing;
    }
}

