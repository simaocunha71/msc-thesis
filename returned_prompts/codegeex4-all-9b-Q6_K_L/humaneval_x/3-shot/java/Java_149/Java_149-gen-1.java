        List<String> result = new ArrayList<>();

        for (String s : lst) {
            if (s.length() % 2 == 0) {
                result.add(s);
            }
        }

        Collections.sort(result, new Comparator<String>() {
            public int compare(String o1, String o2) {
                if (o1.length() > o2.length()) return 1;
                if (o1.length() < o2.length()) return -1;
                return o1.compareTo(o2);
            }
        });
        return result;
    }
}

