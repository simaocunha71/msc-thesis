
      parser.parse(is, handler);
    } catch (Exception e) {
      throw new IllegalArgumentException(
        "Error while parsing managed entity configuration", e);
    }
  }