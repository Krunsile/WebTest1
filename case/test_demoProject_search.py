from base.getDriver import getDriver
from page_objects.pages.indexPage import IndexPage
from assertpy import assert_that
class TestIndex:
    def setup_class(self):
        self.Driver = getDriver()
        self.searchPage=IndexPage(self.Driver.browserOperator).search_kw('test1')

    def test_search_kw(self):
        self.searchPage.search_kw('test2')
        assert_that('test2_百度搜索').is_equal_to(self.Driver.browserOperator.getTitle())

    def teardown_class(self):
        self.Driver.browserOperator.close()