        int[] squares = { a * a, b * b, c * c };
        Arrays.sort(squares);
        return squares[0] + squares[1] == squares[2];
    }
}

