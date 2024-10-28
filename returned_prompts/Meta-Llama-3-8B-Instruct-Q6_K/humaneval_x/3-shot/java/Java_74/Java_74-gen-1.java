        List<String> result = new ArrayList<>();
        int total1 = 0, total2 = 0;

        for (String s : lst1) {
            total1 += s.length();
        }
        for (String s : lst2) {
            total2 += s.length();
        }

        if (total1 < total2) {
            for (String s : lst1) {
                result.add(s);
            }
            return result;
        } else if (total1 > total2) {
            for (String s : lst2) {
                result.add(s);
            }
            return result;
        } else {
            for (String s : lst1) {
                result.add(s);
            }
            return result;
        }
    }
}

