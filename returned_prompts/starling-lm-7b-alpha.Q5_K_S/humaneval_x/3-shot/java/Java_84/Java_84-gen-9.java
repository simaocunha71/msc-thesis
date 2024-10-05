        String result = "";
        while (N > 0) {
            int remainder = N % 2;
            result = remainder + result;
            N /= 2;
        }
        return result;
    }
}

```