
    // Load the configuration settings from the XML file.
    XDocument settings = XDocument.Load("settings.xml");

    // Get the settings for the tile.
    XElement tileElement = settings.Element("tile");
    int tileWidth = (int)tileElement.Attribute("width");
    int tileHeight = (int)tileElement.Attribute("height");

    // Get the settings for the world.
    XElement worldElement = settings.Element("world");
    int worldWidth = (int)worldElement.Attribute("width");
    int worldHeight = (int)worldElement.Attribute("height");

    // Get the settings for the camera.
    XElement cameraElement = settings.Element("camera");
    int cameraSpeed = (int)cameraElement.Attribute("speed");

