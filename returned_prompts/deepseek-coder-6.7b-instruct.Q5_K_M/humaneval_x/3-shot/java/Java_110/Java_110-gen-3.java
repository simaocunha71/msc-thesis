        int oddCount = 0;
        for(int i = 0; i < lst1.size(); i++) {
            if(lst1.get(i) % 2 != 0) {
                oddCount++;
            }
        }
        for(int i = 0; i < lst2.size(); i++) {
            if(lst2.get(i) % 2 == 0) {
                oddCount--;
            }
        }
        return oddCount <= 0 ? "YES" : "NO";
    }
}

