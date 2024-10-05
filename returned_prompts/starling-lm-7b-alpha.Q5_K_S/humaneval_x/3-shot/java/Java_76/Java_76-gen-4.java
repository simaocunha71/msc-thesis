        for (int i = 0; i <= 30; i++) {
            int result = (int) Math.pow(n, i);
            if (result == x) {
                return true;
            }
        }
        return false;
    }
}

