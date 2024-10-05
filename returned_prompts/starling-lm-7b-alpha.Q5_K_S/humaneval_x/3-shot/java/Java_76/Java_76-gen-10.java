        for (int i = 0; i < 100; i++) {
            int number = (int) Math.pow(n, i);
            if (number == x) return true;
        }
        return false;
    }
}

