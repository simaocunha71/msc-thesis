        if (lst1.size() < lst2.size()) {
            return lst1;
        } else if (lst2.size() < lst1.size()) {
            return lst2;
        }
        int sum1 = 0;
        int sum2 = 0;
        for (String s : lst1) {
            sum1 += s.length();
        }
        for (String s : lst2) {
            sum2 += s.length();
        }
        if (sum1 < sum2) {
            return lst1;
        } else if (sum2 < sum1) {
            return lst2;
        } else {
            List<String> result = new ArrayList<>();
            for (String s : lst1) {
                result.add(s);
            }
            return result;
        }
    }
}

