        XmlDocument config = new XmlDocument();
        config.Load("config.xml");

        XmlNode root = config.DocumentElement;
        XmlNode sizeNode = root["Size"];
        int tileSize = int.Parse(sizeNode["TileSize"].InnerText);

        XmlNode worldNode = root["World"];
        int worldWidth = int.Parse(worldNode["Width"].InnerText);
        int worldHeight = int.Parse(worldNode["Height"].InnerText);

        XmlNode cameraNode = root["Camera"];
        float cameraSpeed = float.Parse(cameraNode["Speed"].InnerText);

        // use the settings to set up the game
        Game game = new Game(tileSize, worldWidth, worldHeight, cameraSpeed); 