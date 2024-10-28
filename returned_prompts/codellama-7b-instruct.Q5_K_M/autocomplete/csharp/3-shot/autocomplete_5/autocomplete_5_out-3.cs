
            doc.Load(xml);
            XmlNodeList nodes = doc.GetElementsByTagName("Camera");
            foreach (XmlNode node in nodes)
            {
                foreach (XmlNode node2 in node.ChildNodes)
                {
                    if (node2.Name == "lowSpeed")
                        Camera.lowSpeed = int.Parse(node2.InnerText);
                    else if (node2.Name == "highSpeed")
                        Camera.highSpeed = int.Parse(node2.InnerText);
                }
            }
        }