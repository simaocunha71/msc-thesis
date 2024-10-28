        String path = url.getPath();
        if (path == null) {
          throw new IOException();
        }
        File file = new File(path);
        if (file.exists()) {
          return open(file);
        } else {
          throw new IOException();
        }
      } catch (IOException e) {
        return false;
      }
    }

