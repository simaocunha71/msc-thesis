        int result = Integer.MIN_VALUE;
        for (int i : l) {
            result = Math.max(i, result);
        }
        return result;
    }
}

