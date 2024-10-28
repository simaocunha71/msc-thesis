        int power = 1;
        while (power <= x) {
            if (power == x) {
                return true;
            }
            power *= n;
        }
        return false;
    }
}

