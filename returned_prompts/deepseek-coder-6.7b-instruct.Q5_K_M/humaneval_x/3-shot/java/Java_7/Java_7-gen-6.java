        List<String> filteredStrings = new ArrayList<String>();

        for (String string : strings) {
            if (string.contains(substring)) {
                filteredStrings.add(string);
            }
        }

        return filteredStrings;
     }
}

