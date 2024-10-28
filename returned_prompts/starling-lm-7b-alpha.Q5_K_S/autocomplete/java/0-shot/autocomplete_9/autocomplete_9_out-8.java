      XMLReader reader = parser.getXMLReader();
      reader.setContentHandler(handler);
      reader.parse(new InputSource(is));
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }


