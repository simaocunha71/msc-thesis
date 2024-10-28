```csharp
XmlDocument doc = new XmlDocument();
doc.Load("config.xml");

int tileSize = int.Parse(doc.GetElementsByTagName("tileSize")[0].InnerText);
int worldWidth = int.Parse(doc.GetElementsByTagName("worldWidth")[0].InnerText);
int worldHeight = int.Parse(doc.GetElementsByTagName("worldHeight")[0].InnerText);
int cameraSpeed = int.Parse(doc.GetElementsByTagName("cameraSpeed")[0].InnerText);
```
```
