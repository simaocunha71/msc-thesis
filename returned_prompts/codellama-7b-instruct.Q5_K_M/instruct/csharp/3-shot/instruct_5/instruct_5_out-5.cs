using System;
using System.Xml;

class Program
{
    static void Main(string[] args)
    {
        XmlDocument xmlDoc = new XmlDocument();

        xmlDoc.Load("config.xml");

        XmlNode nodeTileSize = xmlDoc.SelectSingleNode("//config/tile/size");
        XmlNode nodeWorldWidth = xmlDoc.SelectSingleNode("//config/world/width");
        XmlNode nodeWorldHeight = xmlDoc.SelectSingleNode("//config/world/height");
        XmlNode nodeCameraSpeed = xmlDoc.SelectSingleNode("//config/camera/speed");

        // Use the values from the XML file to set the size of a tile, the width and height of a world, and the speed of a camera.
    }
}
