        int limit = (int) Math.sqrt(a);

        for (int i = 2; i <= limit; i++) {
            if (a % i == 0) return false;
        }
        return true;
    }
}

