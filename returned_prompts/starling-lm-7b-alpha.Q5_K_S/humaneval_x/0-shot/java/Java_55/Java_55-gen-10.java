        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int[][] matrix = {
            {1, 1},
            {1, 0}
        };
        int[][] result = matrixPow(matrix, n - 2);
        return result[0][0];
    }

    public static int[][] matrixPow(int[][] a, int b) {
        int n = a.length;
        int[][] r = new int[n][n];
        for (int i = 0; i < n; i++) {
            r[i][i] = 1;
        }
        int[][] c = a;
        while (b > 0) {
            if ((b & 1) == 1) {
                r = mult(r, c);
            }
            c = mult(c, c);
            b >>= 1;
        }
        return r;
    }

    public static int[][] mult(int[][] a, int[][] b) {
        int n = a.length;
        int[][] r = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long sum = 0;
                for (int k = 0; k < n; k++) {
                    sum += (long) a[i][k] * b[k][j];
                }
                r[i][j] = (int) (sum % 1000000007);
            }
        }
        return r;
    }
}



























































































