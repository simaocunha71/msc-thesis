        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }

        for (int num : lst2) {
            if (num % 2 != 0) {
                oddCount--;
            }
        }

        return oddCount <= 0 ? "YES" : "NO";
    }
}

