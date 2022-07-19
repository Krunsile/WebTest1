# 显式等待的类型
class Wait_Type:
    # 判断当前页面的title是否精确等于预期，返回布尔值
    TITLE_IS = 'title_is'
    # 判断当前页面的title是否包含预期字符串，返回布尔值
    TITLE_CONTAINS = 'title_contains'
    # 判断元素是否出现，只要有一个元素出现，返回元素对象
    PRESENCE_OF_ELEMENT_LOCATED = 'presence_of_element_located'
    # 判断元素是否包含指定文本，返回布尔值
    TEXT_TO_BE_PRESENT_IN_ELEMENT = 'text_to_be_present_in_element'
    # 判断某个元素是否被选中,一般用在下拉列表
    ELEMENT_LOCATED_TO_BE_SELECTED = 'element_located_to_be_selected'
    # 判断某个元素是否可见并且是可点击的，如果是的就返回这个元素，否则返回False
    ELEMENT_TO_BE_CLICKABLE = 'element_to_be_clickable'
    # 判断元素是否可见，返回元素对象
    VISIBILITY_OF = 'visibility_of'
    # 判断页面上是否存在alert,如果有就切换到alert并返回alert的内容
    ALERT_IS_PRESENT = 'alert_is_present'
