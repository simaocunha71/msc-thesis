        if (x > y) return -1;
        int result = y - x;
        if (result % 2 == 0) return result;
        if (result == 1) return -1;
        return result - 1;

    }
}

