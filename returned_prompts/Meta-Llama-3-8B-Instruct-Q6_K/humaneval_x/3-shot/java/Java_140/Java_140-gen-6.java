        String[] parts = text.split(" +");
        StringBuilder result = new StringBuilder();
        for (String part : parts) {
            if (result.length() > 0) {
                result.append("_");
            }
            result.append(part);
        }
        return result.toString();
    }
}

