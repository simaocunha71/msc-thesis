        String result = text.replaceAll("\\s+", "_");
        return result.replaceAll("_+", "-");
    }
}

