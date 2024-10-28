        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        for (int num : lst2) {
            if (num % 2 != 0) {
                oddCount--;
                if (oddCount < 0) {
                    return "NO";
                }
            }
        }
        return "YES";
    }
}

