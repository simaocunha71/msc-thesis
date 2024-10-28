        arr.sort((x, y) -> {
            if (Integer.bitCount(x) != Integer.bitCount(y)) {
                return Integer.bitCount(x) - Integer.bitCount(y);
            } else {
                return x - y;
            }
        });
        return arr;
    }
}

