        int result = Integer.MIN_VALUE;

        for (int i : l) {
            result = Math.max(result, i);
        }
        return result;
    }
}

