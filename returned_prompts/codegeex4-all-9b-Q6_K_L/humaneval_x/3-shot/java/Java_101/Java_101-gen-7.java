        List<String> result = new ArrayList<>();
        String[] strings = s.split("[,\\s]+");

        for (String string : strings) {
            result.add(string);
        }

        return result;

    }
}

