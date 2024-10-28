        if (a == 0) {
            return true;
        } else if (a < 0) {
            a = -a;
        }

        double cube = Math.cbrt(a);
        return cube == (int) cube;
    }
}

