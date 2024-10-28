        List<String> ret = new ArrayList<>();
        int total1 = 0;
        for(String str : lst1) {
            total1 += str.length();
        }
        int total2 = 0;
        for(String str : lst2) {
            total2 += str.length();
        }
        if(total1 > total2) {
            return lst1;
        }
        return lst2;
    }
}
