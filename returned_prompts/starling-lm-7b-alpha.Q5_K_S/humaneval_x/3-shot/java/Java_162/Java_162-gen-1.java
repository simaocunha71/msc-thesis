        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] digest = md.digest();
        String result = "";
        for (byte b : digest) {
            result += String.format("%02x", b);
        }
        return Optional.of(result);
    }
}

