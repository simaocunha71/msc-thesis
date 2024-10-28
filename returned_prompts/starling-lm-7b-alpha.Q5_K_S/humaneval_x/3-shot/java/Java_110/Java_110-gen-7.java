        int odd_count = 0;
        for (int i : lst1) {
            if (i % 2 == 1) {
                odd_count += 1;
            }
        }

        if (odd_count == 0) {
            return "YES";
        }

        for (int i : lst2) {
            if (i % 2 == 1) {
                odd_count -= 1;
            }
        }

        if (odd_count == 0) {
            return "YES";
        }

        return "NO";
    }
}

