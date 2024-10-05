        if (!(x instanceof Integer && y instanceof Integer && z instanceof Integer)) return false;
        int a = (int)x;
        int b = (int)y;
        int c = (int)z;
        if (a + b == c) return true;
        if (b + c == a) return true;
        if (a + c == b) return true;
        return false;
    }
}

