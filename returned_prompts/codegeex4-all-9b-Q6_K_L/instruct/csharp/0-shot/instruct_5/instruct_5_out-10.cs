```csharp
using System;
using System.IO;
using System.Xml;

class Program
{
    static void Main()
    {
        string xmlFilePath = "config.xml";
        if (!File.Exists(xmlFilePath))
        {
            Console.WriteLine("The XML file does not exist.");
            return;
        }

        XmlDocument doc = new XmlDocument();
        doc.Load(xmlFilePath);

        XmlNode tileNode = doc.SelectSingleNode("//Tile");
        XmlNode worldWidthNode = doc.SelectSingleNode("//World/Width");
        XmlNode worldHeightNode = doc.SelectSingleNode("//World/Height");
        XmlNode cameraSpeedNode = doc.SelectSingleNode("//Camera/Speed");

        if (tileNode == null || worldWidthNode == null || worldHeightNode == null || cameraSpeedNode == null)
        {
            Console.WriteLine("One or more nodes are missing from the XML file.");
            return;
        }

        int tileSize = int.Parse(tileNode.InnerText);
        int worldWidth = int.Parse(worldWidthNode.InnerText);
        int worldHeight = int.Parse(worldHeightNode.InnerText);
        int cameraSpeed = int.Parse(cameraSpeedNode.InnerText);

        Console.WriteLine($"Tile size: {tileSize}");
        Console.WriteLine($"World width: {worldWidth}");
        Console.WriteLine($"World height: {worldHeight}");
        Console.WriteLine($"Camera speed: {cameraSpeed}");
    }
}
```

