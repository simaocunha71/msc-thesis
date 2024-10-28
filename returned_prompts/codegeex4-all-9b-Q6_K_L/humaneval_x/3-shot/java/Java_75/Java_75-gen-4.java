        if (a < 3) return false;

        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (a % i == 0) return false;
        }

        return true;
    }
}

