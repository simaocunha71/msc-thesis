        if (!(x instanceof Integer)) return false;
        if (!(y instanceof Integer)) return false;
        if (!(z instanceof Integer)) return false;

        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        if (a + b == c) return true;
        else return false;
    }
}
