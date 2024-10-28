        return getBrowser().loadURL(url);
      } catch (Exception e) {
        LOG.error("Error showing document from URL " + url, e);
        return false;
      }
    }

