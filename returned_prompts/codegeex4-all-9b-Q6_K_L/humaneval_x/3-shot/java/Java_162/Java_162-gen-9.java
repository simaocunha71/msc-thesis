        if (text == null || text.equals("")) return Optional.empty();

        MessageDigest md = MessageDigest.getInstance("MD5");
        BigInteger hash = new BigInteger(1, md.digest(text.getBytes()));
        return Optional.of(hash.toString(16));
    }
}

