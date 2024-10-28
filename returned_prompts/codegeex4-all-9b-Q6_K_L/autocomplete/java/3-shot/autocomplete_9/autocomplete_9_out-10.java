      parser.parse(is, handler);
    } catch (ParserConfigurationException e) {
      throw new ConfigurationException(e);
    } catch (SAXException e) {
      throw new ConfigurationException(e);
    } catch (IOException e) {
      throw new ConfigurationException(e);
    }

  }

