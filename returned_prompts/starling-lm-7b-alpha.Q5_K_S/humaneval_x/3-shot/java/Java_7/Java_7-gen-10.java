        List<String> result = new ArrayList<>();
        for (String str : strings) {
            if (str.contains(substring)) result.add(str);
        }
        return result;
    }
}

