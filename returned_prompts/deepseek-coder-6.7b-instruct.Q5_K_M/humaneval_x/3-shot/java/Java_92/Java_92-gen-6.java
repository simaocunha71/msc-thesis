        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        Integer a = (Integer) x;
        Integer b = (Integer) y;
        Integer c = (Integer) z;

        return a + b == c || a + c == b || b + c == a;
    }
}

