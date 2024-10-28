            try
            {
                doc.Load(xml);
                XmlNodeList nodeList = doc.GetElementsByTagName("Camera");
                if (nodeList.Count < 1)
                {
                    System.out.println("No Camera Tag Found");
                }
                else if (nodeList.Count > 1)
                {
                    System.out.println("Multiple Camera Tag Found");
                }
                else
                {
                    XmlNode node = nodeList.Item(0);
                    XmlNode lowSpeedNode = node.SelectSingleNode("lowSpeed");
                    XmlNode highSpeedNode = node.SelectSingleNode("highSpeed");
                    if (lowSpeedNode != null)
                    {
                        lowSpeed = Int32.Parse(lowSpeedNode.InnerText);
                    }
                    if (highSpeedNode != null)
                    {
                        highSpeed = Int32.Parse(highSpeedNode.InnerText);
                    }
                }
            }
            catch (Exception e)
            {
                System.out.println(e.StackTrace);
            }
        }

