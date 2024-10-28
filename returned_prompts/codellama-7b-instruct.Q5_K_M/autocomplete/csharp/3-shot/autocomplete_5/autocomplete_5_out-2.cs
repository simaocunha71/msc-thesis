            doc.LoadXml(xml);
            XmlNodeList nodes = doc.GetElementsByTagName("Camera");
            foreach (XmlNode node in nodes)
            {
                XmlAttributeCollection attributes = node.Attributes;
                foreach (XmlAttribute attribute in attributes)
                {
                    if (attribute.Name == "LowSpeed")
                    {
                        Camera.lowSpeed = attribute.Value;
                    }
                    else if (attribute.Name == "HighSpeed")
                    {
                        Camera.highSpeed = attribute.Value;
                    }
                }
            }
        }

