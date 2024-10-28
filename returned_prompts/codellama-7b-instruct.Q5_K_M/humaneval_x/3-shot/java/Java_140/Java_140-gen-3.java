        String result = text.replaceAll("\\s+", "_");
        result = result.replaceAll("\\s{2,}", "-");
        return result;
    }
}

