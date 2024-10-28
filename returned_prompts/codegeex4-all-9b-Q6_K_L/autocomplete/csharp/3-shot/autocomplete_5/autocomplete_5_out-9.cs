            doc.Load(xml);
            XmlNodeList nodes = doc.GetElementsByTagName("camera");

            foreach (XmlNode node in nodes)
            {
                // Create the camera object
                Camera camera = new Camera();

                // Get the speed attributes and set them on the camera object
               XmlAttribute speedAttribute = node.Attributes["speed"];
                if (speedAttribute != null)
                {
                    int speed;
                    if (int.TryParse(speedAttribute.Value, out speed))
                    {
                        camera.lowSpeed = speed;
                        camera.highSpeed = speed;
                    }
                }
            }
        }
    }

