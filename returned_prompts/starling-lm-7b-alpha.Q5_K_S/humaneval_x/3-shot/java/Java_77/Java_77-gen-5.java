        int b = 0;
        int c = 0;
        while (true) {
            b += 3;
            c = b * b * b;
            if (c == a) return true;
            if (c > a) return false;
        }
    }
}

