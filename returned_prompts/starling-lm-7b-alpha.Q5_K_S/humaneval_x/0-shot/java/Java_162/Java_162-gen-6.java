
    String md5hash = "";
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(text.getBytes());
    byte[] bytes = md.digest();
    StringBuilder sb = new StringBuilder();
    for(int i=0; i< bytes.length; i++)
    {
        sb.append(Integer.toString((bytes[i] & 0xff) + 0x100, 16).substring(1));
    }
    md5hash = sb.toString();

    if(md5hash.length()!=32) return Optional.empty();
    else return Optional.of(md5hash);

    }
}


















```