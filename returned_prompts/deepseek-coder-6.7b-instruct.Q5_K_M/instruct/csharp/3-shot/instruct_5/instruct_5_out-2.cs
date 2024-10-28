XmlDocument doc = new XmlDocument();
doc.Load("config.xml");
XmlNodeList nodes = doc.DocumentElement.SelectNodes("/configuration/appSettings/add");
foreach(XmlNode node in nodes)
{
    string key = node.Attributes["key"].Value;
    string value = node.Attributes["value"].Value;
    if (key == "TileSize")
        TileSize = int.Parse(value);
    else if (key == "WorldWidth")
        WorldWidth = int.Parse(value);
    else if (key == "WorldHeight")
        WorldHeight = int.Parse(value);
    else if (key == "CameraSpeed")
        CameraSpeed = float.Parse(value);
}

