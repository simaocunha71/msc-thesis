        getClass().getMethod("showDocument", URL.class).invoke(this, url);
      }  catch  (Exception e)  {
        System.err.println("Error: " + e.getMessage());
      }
      return true;
    }

