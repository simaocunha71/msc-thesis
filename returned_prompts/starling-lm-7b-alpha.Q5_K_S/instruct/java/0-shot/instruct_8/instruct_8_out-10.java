    public static boolean openURL(String url) {
        boolean ret = true;
        try {
            String[] cmd = { "xdg-open", url };
            Process p = Runtime.getRuntime().exec(cmd);
        } catch (IOException e) {
            ret = false;
        }
        return ret;
    }

