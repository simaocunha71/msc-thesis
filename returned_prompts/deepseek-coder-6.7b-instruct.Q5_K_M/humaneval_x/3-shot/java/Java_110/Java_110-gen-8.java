        int oddInLst1 = 0;
        int oddInLst2 = 0;

        for(int i = 0; i < lst1.size(); i++) {
            if(lst1.get(i) % 2 != 0) {
                oddInLst1++;
            }
        }

        for(int i = 0; i < lst2.size(); i++) {
            if(lst2.get(i) % 2 != 0) {
                oddInLst2++;
            }
        }

        if(oddInLst1 > oddInLst2) {
            return "NO";
        }

        return "YES";
    }
}

