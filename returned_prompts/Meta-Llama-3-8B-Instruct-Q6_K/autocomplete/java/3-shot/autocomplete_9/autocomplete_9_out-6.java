      parser.parse(is, handler);
    } catch (SAXException e) {
      throw new ConfigurationException("Failed to parse config XML",
          e);
    }
  }

