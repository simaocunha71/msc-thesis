            doc.Load(xml);
            XmlNode root = doc.DocumentElement;
            Camera.lowSpeed = int.Parse(root.SelectSingleNode("lowSpeed").InnerText);
            Camera.highSpeed = int.Parse(root.SelectSingleNode("highSpeed").InnerText);
        }
        public static void save(String xml)
        {
            XmlDocument doc = new XmlDocument();
            XmlElement root = doc.CreateElement("camera");
            root.SetAttribute("lowSpeed", Camera.lowSpeed.ToString());
            root.SetAttribute("highSpeed", Camera.highSpeed.ToString());
            doc.AppendChild(root);
            doc.Save(xml);
        }

