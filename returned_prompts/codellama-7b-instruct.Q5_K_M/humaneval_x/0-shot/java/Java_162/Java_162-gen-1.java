        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes(StandardCharsets.UTF_8));
        byte[] digest = md.digest();
        BigInteger bigInt = new BigInteger(1, digest);
        String hashtext = bigInt.toString(16);
        if (hashtext.length() < 32) {
            hashtext = "0" + hashtext;
        }
        return Optional.of(hashtext);
    }
}
