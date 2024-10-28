        String result = text.replace(" ", "_");
        while (result.contains("__")) {
            result = result.replace("__", "-");
        }
        return result;
    }
}

