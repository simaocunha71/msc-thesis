        List<String> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add(String.format("the number of odd elements %dn the str%sng %d of the %snput.", count, str.charAt(0), str.length(), str.length()));
        }
        return result;
    }
}

