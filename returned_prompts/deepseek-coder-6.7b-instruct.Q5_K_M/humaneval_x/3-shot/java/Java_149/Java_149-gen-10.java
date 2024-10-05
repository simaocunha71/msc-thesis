        List<String> result = new ArrayList<>();

        for (String str : lst) {
            if (str.length() % 2 == 0) {
                result.add(str);
            }
        }

        Collections.sort(result, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() != o2.length()) {
                    return o1.length() - o2.length();
                } else {
                    return o1.compareTo(o2);
                }
            }
        });

        return result;
    }
}

