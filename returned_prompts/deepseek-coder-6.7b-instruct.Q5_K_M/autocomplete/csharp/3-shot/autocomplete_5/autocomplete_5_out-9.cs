            doc.LoadXml(xml);

            XmlNodeList nodes = doc.GetElementsByTagName("camera");
            for (int i=0; i < nodes.Count; i++)
            {
                XmlNode node = nodes.Item(i);
                string name = node.Attributes.GetNamedItem("name").Value;
                string model = node.Attributes.GetNamedItem("model").Value;
                string ip = node.Attributes.GetNamedItem("ip").Value;
                int port = int.Parse(node.Attributes.GetNamedItem("port").Value);
                int speed = int.Parse(node.Attributes.GetNamedItem("speed").Value);
                Camera c = new Camera(name, model, ip, port, speed);
                if (speed < Camera.lowSpeed || speed > Camera.highSpeed)
                {
                    throw new Exception("Invalid camera speed: " + speed);
                }
                cameras.Add(c);
            }
         }
