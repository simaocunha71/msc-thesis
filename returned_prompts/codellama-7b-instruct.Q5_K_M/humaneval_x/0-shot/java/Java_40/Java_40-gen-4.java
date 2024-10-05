        for (Integer a : l) {
            for (Integer b : l) {
                for (Integer c : l) {
                    if (a + b + c == 0 && a != b && a != c && b != c) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
