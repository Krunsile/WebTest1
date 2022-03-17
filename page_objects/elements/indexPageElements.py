from page_objects.createElement import CreateElement
from page_objects.wait_type import Wait_Type as Wait_By
from page_objects.locator_type import Locator_Type
class IndexPageElements:
    def __init__(self):
        self.path = '/'
        self.title = CreateElement.create(None,None,None,Wait_By.TITLE_IS,'西南大学')
        self.search_input = CreateElement.create(Locator_Type.ID,'kw',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.search_button =  CreateElement.create(Locator_Type.ID,'su',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)