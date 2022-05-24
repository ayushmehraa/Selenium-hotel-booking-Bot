from selenium import webdriver
import os
import booking.constants as const
from booking.BookingFiltration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Edge):
    def __init__(self,driver_path=r'D:\GitHub Projects\web scrapping\pybookingBot',teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path

        # options=webdriver.ChromeOptions() #for chorm as edge dose support Edgeoption
        # options.add_experimental_option('excludeSwitches',['enable-logging'])
        # super(Booking,self).__init__(options=options)
        
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self,*args):
        if self.teardown:
            self.quit()
    
    def landFirstPage(self):
        self.get(const.BASE_URL)

    def changeCurrency(self,currency=None):
        currency_element=self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()

        selected_currenecy_element=self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="changed_currency=1;selected_currency={currency};top_currency=1"]'
        )
        selected_currenecy_element.click()
    
    def selectPlaceToGo(self,place_to_go):
        searchFieled=self.find_element_by_id("ss")
        searchFieled.clear()
        searchFieled.send_keys(place_to_go)
        first_result=self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    def select_date(self,check_in_date,check_out_date):
        check_in_element=self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element=self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
        
    def select_adults(self,count=2):
        selection_element=self.find_element_by_id('xp__guests__toggle')
        selection_element.click()
        
        while True:
            decrease_adult_count=self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]')
            decrease_adult_count.click()
            adults_value_element=self.find_element_by_id("group_adults")
            adults_value=adults_value_element.get_attribute('value') #gives adult count
            if int(adults_value)==1:
                break
            
        increase_adult_count=self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(1,int(count)):
            increase_adult_count.click()
    
    
    def click_search(self):
        search_button=self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filterations(self):
        filtration=BookingFiltration(driver=self)
        filtration.apply_star_rating(3,4)
        filtration.sort_price_lowest_firdt()
        
    def report_results(self):
        hotel_boxes=self.find_element_by_id("ajaxsrwrap")
        report=BookingReport(hotel_boxes)
        table=PrettyTable(
            ["Hotel Name","Hotel Score","Hotel Price"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)    

