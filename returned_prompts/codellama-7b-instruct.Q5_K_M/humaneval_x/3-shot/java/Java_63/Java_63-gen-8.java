        if (n <= 2) return 0;
        else if (n == 3) return 1;
        else {
            int a = 0;
            int b = 0;
            int c = 1;
            int result = 0;

            for (int i = 0; i < n - 3; i++) {
                result = a + b + c;
                a = b;
                b = c;
                c = result;
            }
            return result;
        }
    }
}

