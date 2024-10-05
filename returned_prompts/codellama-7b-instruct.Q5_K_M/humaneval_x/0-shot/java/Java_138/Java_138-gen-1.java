        for (int i = 2; i <= n; i += 2) {
            if (n - i > 0) {
                if (n - i == i) {
                    continue A;
                } else {
                    return false;
                }
            } else {
                return true;
            }
        }
        return false;
    }
}
