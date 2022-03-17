from base.getDriver import getDriver
from page_objects.pages.indexPage import IndexPage
from assertpy import assert_that
class TestIndex:
    def setup_class(self):
        self.Driver = getDriver()
        self.searchPage=IndexPage(self.Driver.browserOperator).search_kw('apitest')

    # def test_search_kw(self):
    #     self.searchPage.search_kw('apitest12')
    #     assert_that('apitest12_百度搜索').is_equal_to(self.Driver.browserOperator.getTitle())

    def teardown_class(self):
        self.Driver.browserOperator.close()