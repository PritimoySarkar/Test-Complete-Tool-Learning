def Search():
    browser = Sys.Browser()
    pag = browser.Page()
    articles = page.FindElements("")
    Aliases.browser.pageSearch2.Wait()
    #Checks whether the 'contentText' property of the Aliases.browser.pageSearch2.textnodeVeejeeMagneticLearningEn object contains KeywordTests.Search.Variables.SearchKeyword["keyword"].
    aqObject.CheckProperty(Aliases.browser.pageSearch2.textnodeVeejeeMagneticLearningEn, "contentText", cmpContains, Project.Variables.SearchKeyword1.Iterator.Value["keyword"], False)
    Project.Variables.SearchKeyword1.Iterator.Next()
