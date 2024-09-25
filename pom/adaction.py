from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class loginpage:
    
    def __init__(self,bcd):
        self.driver=bcd
        self.__username =self.driver.find_element(By.XPATH,"//input[@type='text']")
        self.__password =self.driver.find_element(By.XPATH,"//input[@type='password']")
        self.__login_button =self.driver.find_element(By.XPATH,"//input[@type='Submit']")
        
        
    def validataloginelement(self):
        assert self.__username.is_displayed()
        assert self.__password.is_displayed()
        assert self.__login_button.is_displayed()
        
    def userloginwithvalidcretentials(self,valid_username,valid_password):
        self.__username.send_keys(valid_username)
        self.__password.send_keys(valid_password)
        self.__login_button.click() 

class searcHoltels:
    def __init__(self,bcd):
       self.driver=bcd
       self.__locations=self.driver.find_element(By.XPATH,"//select[@name='location']")
       self.__hoetels=self.driver.find_element(By.XPATH,"//select[@name='hotels']")
       self.__roomstype=self.driver.find_element(By.XPATH,"//select[@name='room_type']")
       self.__noofrooms=self.driver.find_element(By.XPATH,"//select[@name='room_nos']")
       self.__checkindate=self.driver.find_element(By.XPATH,"//input[@name='datepick_in']")
       self.__checkinout=self.driver.find_element(By.XPATH,"//input[@name='datepick_out']")
       self.__adultperroom=self.driver.find_element(By.XPATH,"//select[@name='adult_room']")
       self.__childprroom=self.driver.find_element(By.XPATH,"//select[@name='child_room']")
       self.__searchbutton=self.driver.find_element(By.XPATH,"//input[@type='submit']")
    
    def validatesearchotel(self):
        assert self.__locations.is_displayed()
        assert self.__hoetels.is_displayed()
        assert self.__roomstype.is_displayed()
        assert self.__noofrooms.is_displayed()
        assert self.__checkindate.is_displayed()
        assert self.__checkinout.is_displayed()
        assert self.__adultperroom.is_displayed()
        assert self.__childprroom.is_displayed()
        assert self.__searchbutton.is_displayed()

    def searchHotel(self,date,out):
        self.sc=Select(self.__locations)
        self.sc.select_by_index(5)
        self.sc=Select(self.__hoetels)
        self.sc.select_by_index(2)
        self.sc=Select(self.__roomstype)
        self.sc.select_by_index(1)
        self.sc=Select(self.__noofrooms)
        self.sc.select_by_index(1)
        self.__checkindate.clear()
        self.__checkindate.send_keys(date)
        self.__checkinout.clear()
        self.__checkinout.send_keys(out)
        self.sc=Select(self.__adultperroom)
        self.sc.select_by_index(2)
        self.sc=Select(self.__childprroom)
        self.sc.select_by_index(0)
        self.__searchbutton.click()

class selecthotelbook:
    def __init__(self,bcd):
        self.driver=bcd
        self.__selectedhotel=self.driver.find_element(By.XPATH,"//input[@name='radiobutton_0']")
        self.__coninue=self.driver.find_element(By.XPATH,"//input[@type='submit']")

    def hotelbuttonmark(self):
        assert self.__coninue.is_displayed()

    def clickthebutton(self):
        self.__selectedhotel.click()
        self.__coninue.click()

class bookahotel:

    def __init__(self,bcd):
        self.driver=bcd
        self.__firstname=self.driver.find_element(By.XPATH,"//input[@name='first_name']")
        self.__lastname=self.driver.find_element(By.XPATH,"//input[@name='last_name']")
        self.__billingaddress=self.driver.find_element(By.XPATH,"//textarea[@name='address']")
        self.__cardnumber=self.driver.find_element(By.XPATH,"//input[@name='cc_num']")
        self.__cardtype=self.driver.find_element(By.XPATH,"//select[@name='cc_type']")
        self.__expiarydate=self.driver.find_element(By.XPATH,"//select[@name='cc_exp_month']")
        self.__expiarydate1=self.driver.find_element(By.XPATH,"//select[@name='cc_exp_year']")
        self.__ccvnumber=self.driver.find_element(By.XPATH,"//input[@name='cc_cvv']")
        self.__booknow=self.driver.find_element(By.XPATH,"//input[@type='button']")

    def assertvalues(self):
        assert self.__firstname.is_displayed()
        assert self.__lastname.is_displayed()
        assert self.__billingaddress.is_displayed()
        assert self.__cardnumber.is_displayed()
        assert self.__cardtype.is_displayed()
        assert self.__expiarydate.is_displayed()
        assert self.__expiarydate1.is_displayed()
        assert self.__ccvnumber.is_displayed()
        assert self.__booknow.is_displayed()

    def valuesinset(self,F,L,BA,CN,CCVN):
        self.__firstname.send_keys(F)
        self.__lastname.send_keys(L)
        self.__billingaddress.send_keys(BA)
        self.__cardnumber.send_keys(CN)
        self.sc=Select(self.__cardtype)
        self.sc.select_by_index(2)
        self.sc=Select(self.__expiarydate)
        self.sc.select_by_index(11)
        self.sc=Select(self.__expiarydate1)
        self.sc.select_by_index(14)
        self.__ccvnumber.send_keys(CCVN)
        self.__booknow.click()

class myhistory:
    def __init__(self,bcd):
        self.driver=bcd
        time.sleep(5)
        self.__history=self.driver.find_element(By.XPATH,"(//input[@type='button'])[2]")

    def clickhistory(self):
        assert self.__history.is_displayed()

    def opened(self):
        self.__history.click()

class finalprocess():
    def __init__(self,bcd):
        self.driver=bcd
        self.__click=self.driver.find_element(By.XPATH,"//input[@name='ids[]']")
        self.__cancelselected=self.driver.find_element(By.XPATH,"//input[@name='cancelall']")

    def assertfinalprocess(self):
      assert self.__click.is_displayed()    
      assert self.__cancelselected.is_displayed()

    def finished(self,):
        self.__click.click()
        self.__cancelselected.click()
        self.driver.switch_to.alert.accept()
        print("******project is successfully executed******")
          