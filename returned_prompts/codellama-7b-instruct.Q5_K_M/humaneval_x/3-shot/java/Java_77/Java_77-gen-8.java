        for (int i = 1; i * i * i <= a; i++) {
            if (a == i * i * i) {
                return true;
            }
        }
        return false;
    }
}

