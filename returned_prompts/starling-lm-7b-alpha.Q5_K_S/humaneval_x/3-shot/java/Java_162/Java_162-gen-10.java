        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] digest = md.digest();
        BigInteger bigInt = new BigInteger(1, digest);
        String md5 = bigInt.toString(16);
        if (md5.length() < 32) {
            md5 = "0" + md5;
        }
        return Optional.of(md5);
    }
}

