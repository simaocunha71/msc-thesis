        List<String> result = new ArrayList<>();
        for (String str : lst) {
            if (str.length() % 2 == 0) {
                result.add(str);
            }
        }
        Collections.sort(result);
        return result;

    }
}

