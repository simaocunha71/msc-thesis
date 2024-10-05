        List<String> result = new ArrayList<>();

        for (String string : strings) {
            if (string.contains(substring)) {
                result.add(string);
            }
        }

        return result;
    }
}


A: The code provided by you is correct. It filters an input list of strings only for ones that contain given substring. It uses the contains() method of the String class to check if the string contains the substring. If it does, it adds the string to the result list.
