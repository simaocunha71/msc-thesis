        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int a = (int) x;
            int b = (int) y;
            int c = (int) z;

            return a + b == c || a + c == b || b + c == a;
        }
        return false;
    }
}

