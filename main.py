import pytest
import allure
import os

if __name__ == '__main__':

    # pytest.main(["-v", "-s", "./case"])
    # 执行pytest，生成 Allure 报告需要的数据存在 /result 目录
    pytest.main(['--alluredir', './result'])
    # 执行命令生成测试报告
    os.system('allure generate ./result -o ./report --clean')