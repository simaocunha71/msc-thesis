        String[] result = txt.split("\\s+");
        if (result.length > 0) return result;
        else return txt.split(",");
    }
}

