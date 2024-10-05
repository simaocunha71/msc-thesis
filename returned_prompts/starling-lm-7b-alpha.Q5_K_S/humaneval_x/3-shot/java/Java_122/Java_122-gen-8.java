        int result = 0;
        for (int i = 0; i < k; i++) {
            if (arr.get(i) < 10) result += arr.get(i);
            else if (arr.get(i) < 100) result += arr.get(i) % 10 + arr.get(i) / 10;
        }
        return result;
    }
}

