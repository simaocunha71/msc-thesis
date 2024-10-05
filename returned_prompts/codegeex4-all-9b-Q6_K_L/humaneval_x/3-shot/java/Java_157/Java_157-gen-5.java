        int max_side = Math.max(a, Math.max(b, c));

        if (max_side == a) {
            return (b * b + c * c) == a * a;
        } else if (max_side == b) {
            return (a * a + c * c) == b * b;
        } else {
            return (a * a + b * b) == c * c;
        }
    }
}

