        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        int a = (Integer) x, b = (Integer) y, c = (Integer) z;
        if (a + b == c) return true;
        else return false;
    }
}


