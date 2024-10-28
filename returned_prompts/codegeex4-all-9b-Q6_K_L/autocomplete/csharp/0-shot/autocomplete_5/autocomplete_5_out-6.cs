 doc.Load(xml);
            XmlNodeList nodes = doc.DocumentElement.SelectNodes("/cameras/camera");
            foreach (XmlNode node in nodes)
            {
                String name = node.Attributes["name"].Value;
                int speed = Convert.ToInt32(node.Attributes["speed"].Value);
                if (speed > Camera.highSpeed)
                {
                    Camera.highSpeed = speed;
                }
                else if (speed < Camera.lowSpeed)
                {
                    Camera.lowSpeed = speed;
                }
            }
        }

```csharp
            Camera camera = new Camera();
            camera.name = name;
            camera.speed = speed;
            cameras.Add(camera);
        }
    }
}
```