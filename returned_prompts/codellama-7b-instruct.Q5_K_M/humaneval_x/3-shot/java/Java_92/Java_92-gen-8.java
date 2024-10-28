        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int a = (int) x;
            int b = (int) y;
            int c = (int) z;
            if (a == b + c) {
                return true;
            }
        }
        return false;
    }
}

