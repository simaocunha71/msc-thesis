        Document doc = Jsoup.connect(url.toString()).get();
        Elements links = doc.select("a[href]");
        int size = links.size();
        for (int i = 0; i < size; i++) {
          if (links.get(i).attr("href").indexOf("https://") == -1) {
            return false;
          }
        }
        return true;
      } catch (IOException e) {
        e.printStackTrace();
        return false;
      }
    }

