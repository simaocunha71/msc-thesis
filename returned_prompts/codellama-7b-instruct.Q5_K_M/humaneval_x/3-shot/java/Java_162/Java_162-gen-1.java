        if (text.length() == 0) return Optional.empty();
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] md5hash = md.digest();
        BigInteger bigInt = new BigInteger(1, md5hash);
        String output = bigInt.toString(16);
        while (output.length() < 32) {
            output = "0" + output;
        }
        return Optional.of(output);
    }
}

