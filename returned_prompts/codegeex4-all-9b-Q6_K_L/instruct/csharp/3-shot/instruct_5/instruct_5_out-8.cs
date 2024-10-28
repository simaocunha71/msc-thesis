```csharp
using System;
using System.IO;
using System.Xml;

class Program
{
    static void Main()
    {
        string xmlFilePath = "config.xml";
        if (File.Exists(xmlFilePath))
        {
            try
            {
                XmlDocument xmlDoc = new XmlDocument();
                xmlDoc.Load(xmlFilePath);

                XmlNode tileNode = xmlDoc.SelectSingleNode("/config/tile");
                if (tileNode != null)
                {
                    int tileSize = int.Parse(tileNode.InnerText);
                    Console.WriteLine($"Tile Size: {tileSize}");
                }

                XmlNode worldNode = xmlDoc.SelectSingleNode("/config/world");
                if (worldNode != null)
                {
                    int worldWidth = int.Parse(worldNode.SelectSingleNode("width").InnerText);
                    int worldHeight = int.Parse(worldNode.SelectSingleNode("height").InnerText);
                    Console.WriteLine($"World Width: {worldWidth}, Height: {worldHeight}");
                }

                XmlNode cameraNode = xmlDoc.SelectSingleNode("/config/camera");
                if (cameraNode != null)
                {
                    int cameraSpeed = int.Parse(cameraNode.SelectSingleNode("speed").InnerText);
                    Console.WriteLine($"Camera Speed: {cameraSpeed}");
                }
            }
            catch (XmlException ex)
            {
                Console.WriteLine($"Error loading XML: {ex.Message}");
            }
            catch (FormatException ex)
            {
                Console.WriteLine($"Error parsing value: {ex.Message}");
            }
        }
        else
        {
            Console.WriteLine($"XML file not found: {xmlFilePath}");
        }
    }
}
```
