import unittest
from HTMLTestRunner import HTMLTestRunner
from api.base import Base

if __name__=="__main__":
    base=Base()
    base.login()
    suite=unittest.TestLoader().discover("cases",pattern="test*.py")
    with open("test_report","wb") as f:
        runner= HTMLTestRunner(f,title="标题",description="测试用户")
        runner.run(suite)
