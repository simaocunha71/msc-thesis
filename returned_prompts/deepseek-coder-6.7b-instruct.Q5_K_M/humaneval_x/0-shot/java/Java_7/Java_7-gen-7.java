        List<String> result = new ArrayList<>();
        for (String string : strings) {
            if (string.contains(substring)) {
                result.add(string);
            }
        }
        return result;
    }
}

This is a simple Java solution. We create a new ArrayList to store the result. For each string in the given list, we check if it contains the substring. If it does, we add it to the result list. Finally, we return the result list.


