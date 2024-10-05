        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] digest = md.digest();
        String result = "";
        for (byte b : digest) {
            String hexString = Integer.toHexString(b);
            if (hexString.length() == 1) {
                result += "0";
            }
            result += hexString;
        }
        return Optional.of(result);
    }
}

