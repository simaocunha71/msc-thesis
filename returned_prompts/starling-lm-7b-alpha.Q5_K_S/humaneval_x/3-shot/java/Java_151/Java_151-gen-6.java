        int result = 0;
        for (Object obj : lst) {
            int n = (int) obj;
            if (n < 0 || (n & 1) == 0) continue;
            result += n * n;
        }
        return result;
    }
}


