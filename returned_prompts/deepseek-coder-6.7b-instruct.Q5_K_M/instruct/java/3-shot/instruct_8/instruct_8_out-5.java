public boolean openWebPage(String url) {
    try {
        Desktop.getDesktop().browse(new URI(url));
        return true;
    } catch (IOException | URISyntaxException e) {
        return false;
    }
}

