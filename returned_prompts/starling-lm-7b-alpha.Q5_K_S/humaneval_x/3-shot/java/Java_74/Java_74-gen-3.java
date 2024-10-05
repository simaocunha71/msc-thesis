        if (lst1.size() < lst2.size()) {
            return lst1;
        } else if (lst1.size() > lst2.size()) {
            return lst2;
        }

        List<String> result = new ArrayList<>();
        for (String s1 : lst1) {
            boolean found = false;
            for (String s2 : lst2) {
                if (s1.equals(s2)) {
                    result.add(s1);
                    found = true;
                    break;
                }
            }
            if (!found) {
                return result;
            }
        }
        return result;
    }
}

