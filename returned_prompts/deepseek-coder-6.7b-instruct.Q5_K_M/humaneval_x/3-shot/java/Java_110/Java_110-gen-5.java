        int oddLst1Count = (int)lst1.stream().filter(i -> i % 2 != 0).count();
        int oddLst2Count = (int)lst2.stream().filter(i -> i % 2 != 0).count();

        if(oddLst1Count > oddLst2Count) {
            return "NO";
        }

        return "YES";
    }
}

