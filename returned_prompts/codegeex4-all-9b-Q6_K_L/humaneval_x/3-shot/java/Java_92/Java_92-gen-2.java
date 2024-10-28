        if (x instanceof Double || y instanceof Double || z instanceof Double) {
            return false;
        }

        int a = (int) x;
        int b = (int) y;
        int c = (int) z;

        return a == b + c || b == a + c || c == a + b;
    }
}

