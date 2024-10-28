      parser.parse(is, handler);
    }  catch  (ParserConfigurationException e)  {
      throw new AssertionError(e);
    }  catch  (SAXException e)  {
      throw new AssertionError(e);
    }  catch  (IOException e)  {
      throw new AssertionError(e);
    }
  }

