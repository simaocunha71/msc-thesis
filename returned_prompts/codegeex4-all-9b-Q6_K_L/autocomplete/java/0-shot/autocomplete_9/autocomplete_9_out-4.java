      parser.parse(is, handler);
    } catch (SAXException e) {
      throw new IllegalArgumentException("Configuration file contains "
 + "invalid XML: " + e);
    } catch (ParserConfigurationException e) {
      throw new IllegalArgumentException("Parser configuration error: "
 + e);
    } catch (IOException e) {
      throw new IllegalArgumentException("I/O error reading configuration "
 + "file: " + e);
    }
  }

