        List<String> result = new ArrayList<>();
        for (String str : lst) {
            if (str.length() % 2 == 0) result.add(str);
        }
        Collections.sort(result, (a, b) -> a.length() == b.length() ? a.compareTo(b) : Integer.compare(a.length(), b.length()));
        return result;
    }
}

