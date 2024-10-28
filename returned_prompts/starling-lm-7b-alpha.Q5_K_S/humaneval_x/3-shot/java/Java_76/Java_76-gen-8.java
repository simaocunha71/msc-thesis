        int power = 0;
        while (x > 0) {
            x /= n;
            power += 1;
        }
        return power == 1;
    }
}

