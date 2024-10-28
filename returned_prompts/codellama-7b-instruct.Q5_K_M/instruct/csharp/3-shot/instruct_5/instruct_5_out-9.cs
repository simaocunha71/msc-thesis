
    For example, if the XML file contains the following:
    ```xml
    <settings>
      <tileSize>100</tileSize>
      <worldWidth>10</worldWidth>
      <worldHeight>10</worldHeight>
      <cameraSpeed>5</cameraSpeed>
    </settings>
    ```
    your program should return the following:
    ```csharp
    var tileSize = 100;
    var worldWidth = 10;
    var worldHeight = 10;
    var cameraSpeed = 5;
    ```

    You can use the following as a starting point:
    ```csharp
    // Get the path to the file
    var path = @"C:\settings.xml";

    // Load the file
    var xml = XElement.Load(path);

    // Get the tile size
    var tileSize = int.Parse(xml.Element("tileSize").Value);

    // Get the world width
    var worldWidth = int.Parse(xml.Element("worldWidth").Value);

    // Get the world height
    var worldHeight = int.Parse(xml.Element("worldHeight").Value);

    // Get the camera speed
    var cameraSpeed = int.Parse(xml.Element("cameraSpeed").Value);

    // Return the values
    return $"var tileSize = {tileSize};" +
           $"var worldWidth = {worldWidth};" +
           $"var worldHeight = {worldHeight};" +
           $"var cameraSpeed = {cameraSpeed};";
    ```

    Note:
    * You can use the `XElement.Load` method to load an XML file.
    * You can use the `Element` method to get an element from an `XElement`.
    * You can use the `Value` property to get the value of an element.
    * The `Parse` method can be used to convert a string to an integer.
    * You can use string interpolation to generate a string.

    This is a classic problem, and many people have used different techniques to solve it.
    You can choose any technique, or use a combination of techniques.

    * Use `XElement.