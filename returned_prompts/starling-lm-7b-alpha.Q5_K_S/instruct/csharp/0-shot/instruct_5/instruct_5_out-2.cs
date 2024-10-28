
```csharp
using System;
using System.Xml.Serialization;

[XmlRoot("Settings")]
public class Settings
{
    [XmlElement("tileSize")]
    public int TileSize { get; set; }

    [XmlElement("worldWidth")]
    public int WorldWidth { get; set; }

    [XmlElement("worldHeight")]
    public int WorldHeight { get; set; }

    [XmlElement("cameraSpeed")]
    public int CameraSpeed { get; set; }
}

public static void Main()
{
    Settings settings;
    using (var reader = XmlReader.Create("config.xml"))
    {
        var serializer = new XmlSerializer(typeof(Settings));
        settings = (Settings)serializer.Deserialize(reader);
    }

    Console.WriteLine("Tile size: {0}", settings.TileSize);
    Console.WriteLine("World width: {0}", settings.WorldWidth);
    Console.WriteLine("World height: {0}", settings.WorldHeight);
    Console.WriteLine("Camera speed: {0}", settings.CameraSpeed);
}
```

In this code, we define a `Settings` class with properties for `tileSize`, `worldWidth`, `worldHeight`, and `cameraSpeed`. The class is marked with the `[XmlRoot]` attribute to specify the root element of the XML file.

In the `Main` method, we create an instance of `Settings` and use the `XmlReader` class to read the XML file named "config.xml". We then use the `XmlSerializer` to deserialize the XML content into the `settings` object.

Finally, we print the values of the properties to the console using `Console.WriteLine`.

To use this code, make sure you have an XML file named "config.xml" in the same directory as your program, with the following content:

```xml
<Settings>
    <tileSize>32</tileSize>
    <worldWidth>100</worldWidth>
    <worldHeight>100</worldHeight>
    <cameraSpeed>5</cameraSpeed>
</Settings>
```

This XML file defines the values for the `tileSize`, `worldWidth