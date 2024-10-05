        String[] split_string = s.split(" |,");
        List<String> result = new ArrayList<>();
        for (String str : split_string) {
            result.add(str);
        }
        return result;
    }
}

