from pom.adaction import loginpage
from selenium import webdriver
from pom.adaction import searcHoltels
from pom.adaction import selecthotelbook
from pom.adaction import bookahotel
from pom.adaction import myhistory
from pom.adaction import finalprocess

def test_login():
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("detach",True)
    opt.add_argument("--incognito")
    driver=webdriver.Chrome(options=opt)
    driver.get("https://adactinhotelapp.com/")
    lp=loginpage(driver)
    lp.validataloginelement()
    lp.userloginwithvalidcretentials("Gokul1023007","gokulsaga1023007")
    lp=searcHoltels(driver)
    lp.validatesearchotel()
    lp.searchHotel('07/01/2024',"08/01/2024")
    lp=selecthotelbook(driver)
    lp.hotelbuttonmark()
    lp.clickthebutton()
    lp=bookahotel(driver)
    lp.assertvalues()
    lp.valuesinset("gokul","selvaraj","10/kundrathur",1029384756564739,227)
    lp=myhistory(driver)
    lp.clickhistory()
    lp.opened()
    lp=finalprocess(driver)
    lp.assertfinalprocess()
    lp.finished()