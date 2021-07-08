def SearchTable(key):
    url = "https://en.wikipedia.org/wiki/Life_Is_Strange"
    #Browsers.Item[btChrome].Run(url)
    Browsers.Item[btChrome].Navigate(url)
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    page = Sys.Browser("*").Page("*")
    
    #table = page.WaitElement("xpath://table[@class='wikitable'][2]")
    # You can also use the FindChild method
    #table = page.FindChild("table", "table", 10)
    table = page.FindChildByXPath("//table[@class='wikitable'][2]", True);
    if table.Exists:
      # Goes through the rows and cells of the table
      for i in range (0, table.rows.length):
        #Log.AppendFolder("Row " + IntToStr(i))
        for j in range (0, table.rows.item(i).cells.length):
          if(table.rows.item(i).cells.item(j).innerText == key):
            Log.Message("Search Keyword found at row: "+ IntToStr(i) + " and colum: " + IntToStr(j))
          #Log.Message("Cell " + IntToStr(j) + ": " + table.rows.item(i).cells.item(j).innerText)
        #Log.PopLogFolder()
    else:
      Log.Warning("The table was not found")