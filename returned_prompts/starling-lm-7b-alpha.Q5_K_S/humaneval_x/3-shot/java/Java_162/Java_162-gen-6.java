        MessageDigest digest = MessageDigest.getInstance("MD5");
        digest.update(text.getBytes(StandardCharsets.UTF_8));
        byte[] md5 = digest.digest();
        StringBuilder result = new StringBuilder();
        for (byte b : md5) {
            result.append(String.format("%02x", b));
        }
        return Optional.of(result.toString());
    }
}

