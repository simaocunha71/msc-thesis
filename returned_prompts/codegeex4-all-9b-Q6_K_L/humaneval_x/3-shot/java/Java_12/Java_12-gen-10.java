        if (strings.size() == 0) return Optional.empty();
        String result = strings.get(0);
        for (String s : strings) {
            if (s.length() > result.length()) result = s;
        }
        return Optional.of(result);
    }
}

