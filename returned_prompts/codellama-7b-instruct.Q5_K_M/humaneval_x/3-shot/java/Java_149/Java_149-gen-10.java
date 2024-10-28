        lst.sort((str1, str2) -> {
            if (str1.length() != str2.length()) return str1.length() - str2.length();
            return str1.compareTo(str2);
        });
        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) result.add(s);
        }
        return result;
    }
}

