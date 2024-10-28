        String result = text.replaceAll(" +", "_");
        result = result.replaceAll("  ", "-");
        return result;
    }
}

