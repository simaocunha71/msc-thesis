        XmlDocument xmlDoc = new XmlDocument();
        xmlDoc.Load(ConfigurationFile);

        XmlNodeList nodeList = xmlDoc.SelectNodes("//World/Size");
        if (nodeList.Count > 0)
        {
            Size = int.Parse(nodeList[0].InnerText);
        }
        else
        {
            Size = 50;
        }

        nodeList = xmlDoc.SelectNodes("//World/Width");
        if (nodeList.Count > 0)
        {
            Width = int.Parse(nodeList[0].InnerText);
        }
        else
        {
            Width = 1000;
        }

        nodeList = xmlDoc.SelectNodes("//World/Height");
        if (nodeList.Count > 0)
        {
            Height = int.Parse(nodeList[0].InnerText);
        }
        else
        {
            Height = 1000;
        }

        nodeList = xmlDoc.SelectNodes("//Camera/Speed");
        if (nodeList.Count > 0)
        {
            Speed = float.Parse(nodeList[0].InnerText);
        }
        else
        {
            Speed = 0.05f;
        }

