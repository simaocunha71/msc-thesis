        if (x instanceof Double || y instanceof Double || z instanceof Double) return false;

        int a = (int) x;
        int b = (int) y;
        int c = (int) z;

        if (a + b == c || a + c == b || b + c == a) return true;
        return false;
    }
}

