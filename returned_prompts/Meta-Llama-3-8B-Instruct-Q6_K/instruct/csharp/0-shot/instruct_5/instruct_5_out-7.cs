    ```csharp
    using System;
    using System.Xml;
    using System.IO;

    class Program
    {
        static void Main()
        {
            XmlDocument xmlDocument = new XmlDocument();
            xmlDocument.Load("config.xml");

            XmlElement root = xmlDocument.DocumentElement;
            XmlNode tileSizeNode = root.SelectSingleNode("tileSize");
            int tileSize = Convert.ToInt32(tileSizeNode.InnerText);

            XmlNode worldSizeNode = root.SelectSingleNode("worldSize");
            int worldWidth = Convert.ToInt32(worldSizeNode.SelectSingleNode("width").InnerText);
            int worldHeight = Convert.ToInt32(worldSizeNode.SelectSingleNode("height").InnerText);

            XmlNode cameraSpeedNode = root.SelectSingleNode("cameraSpeed");
            float cameraSpeed = float.Parse(cameraSpeedNode.InnerText);

            Console.WriteLine("Tile size: {0}", tileSize);
            Console.WriteLine("World width: {0}", worldWidth);
            Console.WriteLine("World height: {0}", worldHeight);
            Console.WriteLine("Camera speed: {0}", cameraSpeed);
        }
    }
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp
```  ```csharp