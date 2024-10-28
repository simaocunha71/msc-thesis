    public List<String> listSort(List<String> lst) {
        lst.removeIf(str -> str.length() % 2 != 0);
        Collections.sort(lst, (str1, str2) -> {
            if (str1.length() == str2.length()) {
                return str1.compareTo(str2);
            } else {
                return Integer.compare(str1.length(), str2.length());
            }
        });
        return lst;
    }