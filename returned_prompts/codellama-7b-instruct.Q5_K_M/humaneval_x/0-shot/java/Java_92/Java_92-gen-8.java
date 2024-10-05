        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            if (((Integer) x + (Integer) y) == (Integer) z) return true;
            else return false;
        } else {
            return false;
        }
    }
}


