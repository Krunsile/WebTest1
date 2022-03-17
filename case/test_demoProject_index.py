from base.getDriver import getDriver
from page_objects.pages.indexPage import IndexPage
from assertpy import assert_that
class TestIndex:
    def setup_class(self):
        self.Driver = getDriver()
        self.indexPage=IndexPage(self.Driver.browserOperator)

    def test_search_empty_kw(self):
        # self.indexPage.search_kw('')
        assert_that(self.indexPage.getElements().title.wait_expected_value).is_equal_to(self.Driver.browserOperator.getTitle())
    #
    # def test_search_kw(self):
    #     self.indexPage.search_kw('西南大学')
    #     # assert_that('西南大学_百度搜索').is_equal_to(self.Driver.browserOperator.getTitle())

    def teardown_class(self):
        self.Driver.browserOperator.close()