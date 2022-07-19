import pytest
import os
import shutil

if __name__ == '__main__':

    shutil.rmtree('./result')
    # 执行pytest，生成 Allure 报告需要的数据存在 /result 目录
    pytest.main(['--alluredir', './result'])
    # 生成测试报告
    os.system('allure generate ./result -o ./report --clean')
    os.system('allure open ./report')

