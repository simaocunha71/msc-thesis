        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        if (oddCount > lst2.size()) {
            return "NO";
        } else {
            return "YES";
        }
    }
}

