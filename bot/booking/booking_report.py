#This fiile is going have methods that will parse specific data we need from one of the deal boxes 

from selenium.webdriver.remote.webelement import WebElement
class BookingReport:
    def __init__(self,boxes_section_element:WebElement):
        self.boxes_section_element=boxes_section_element  
        self.deal_boxs=self.pull_deal_boxes()  

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
            )
        
    def pull_deal_box_attributes(self):
        collection=[]
        for deal_box in self.deal_boxs:
            try:
                # pulling the holte name
                hotel_name=deal_box.find_element_by_css_selector(
                    'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()

                # puling prices
                hotel_price=deal_box.find_element_by_class_name(
                    '_e885fdc12'
                ).get_attribute('innerHTML').strip()
                # hotel score
                hotel_score=deal_box.find_element_by_class_name(
                    'bd528f9ea6'
                ).get_attribute('innerHTML').strip()

                collection.append(
                    [hotel_name,hotel_score,hotel_price]
                )
                # print(hotel_name)
            except :
                continue       

        return collection

            
            
    


           

        