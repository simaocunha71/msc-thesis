        if (n < 4 || n % 2 == 1) return false;
        return isSumEven(n, 4);
    }

    private boolean isSumEven(int n, int target) {
        if (target == 0) return true;
        if (n < 4 || n < target * 2) return false;
        return isSumEven(n - target * 2, target - 1);
    }
}

