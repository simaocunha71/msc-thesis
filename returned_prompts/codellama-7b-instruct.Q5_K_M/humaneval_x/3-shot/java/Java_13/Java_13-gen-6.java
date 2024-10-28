        while (b != 0) {
            int old_b = b;
            b = a % b;
            a = old_b;
        }
        return a;
    }
}

