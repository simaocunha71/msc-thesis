        Collections.sort(arr, (a, b) -> Integer.compare(
            Integer.bitCount(a),
            Integer.bitCount(b)) != 0
                ? Integer.compare(Integer.bitCount(a), Integer.bitCount(b))
                : Integer.compare(a, b));
        return arr;
    }
}

