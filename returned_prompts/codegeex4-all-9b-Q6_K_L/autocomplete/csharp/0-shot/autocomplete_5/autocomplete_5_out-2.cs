            doc.Load(xml);
            XmlNodeList nodes = doc.GetElementsByTagName("Camera");
            foreach (XmlNode node in nodes)
            {
                string name = node.Attributes["name"].Value;
                int speed = int.Parse(node.Attributes["speed"].Value);
                if (speed < 30)
                    Camera.lowSpeed++;
                else
                    Camera.highSpeed++;
            }
        }

