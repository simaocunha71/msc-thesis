        List<String> result = new ArrayList<>();
        for (String s : lst) {
            result.add(s.replaceAll(".", "n"));
            result.add(s.replaceAll("[02468]", ""));
            result.add(s.replaceAll("[13579]", "n"));
        }
        return result;
    }
}

