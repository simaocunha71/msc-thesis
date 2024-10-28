
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().browse(url.toURI());
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening URL: " + url, e);
      }
      return false;
    }


    @Override
    public boolean showDocument(URI uri) {
      try {
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().browse(uri);
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening URI: " + uri, e);
      }
      return false;
    }

    @Override
    public boolean showDocument(String url) {
      try {
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().browse(new URI(url));
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening URL: " + url, e);
      }
      return false;
    }

    @Override
    public boolean showDocument(File file) {
      try {
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().open(file);
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening file: " + file, e);
      }
      return false;
    }



    @Override
    public boolean openFile(File file) {
      try {
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().open(file);
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening file: " + file, e);
      }
      return false;
    }

    @Override
    public boolean openFile(String file) {
      try {
        if (Desktop.isDesktopSupported()) {
          Desktop.getDesktop().open(new File(file));
          return true;
        }
      } catch (Exception e) {
        log.error("Error opening file: " + file, e);