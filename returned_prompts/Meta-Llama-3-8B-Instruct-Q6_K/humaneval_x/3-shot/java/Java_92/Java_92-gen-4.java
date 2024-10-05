        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        return (a == b + c) || (a == c + b) || (b == a + c) || (b == c + a) || (c == a + b) || (c == b + a);
    }
}

