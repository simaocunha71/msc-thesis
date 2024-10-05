        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int a = (Integer) x;
            int b = (Integer) y;
            int c = (Integer) z;

            return a == b + c || b == a + c || c == a + b;
        }
        return false;
     }
}

