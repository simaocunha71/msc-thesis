        Collections.sort(arr, (x, y) -> Integer.compare(Integer.bitCount(x), Integer.bitCount(y))
                .thenComparingInt(x, y));
        return arr;
    }
}

