import unittest
from api.manage_user import UserManager
from loguru import logger
from data.UserManageData import UserManageData

class TestUserManager(unittest.TestCase):
    userid=0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user=UserManager()
        cls.user.login()
        cls.username=UserManageData.add_user_data.get("username")
        cls.password =UserManageData.add_user_data.get("password")
        cls.newusername="testj211"

    def test01_add_user(self):
        self.user_id=None
        actual_result=self.user.user_add(self.username,self.password)
        data=actual_result.get("data")
        if actual_result:
            self.user_id=data.get("id")
            TestUserManager.userid=self.user_id
            logger.info("添加管理员的id是{}".format(TestUserManager.userid))
        self.assertEqual(0,actual_result["errno"])
        self.assertEqual(self.username,actual_result.get("data").get("username"))

    def test02_edit_user(self):
        actual_result = self.user.user_edit(TestUserManager.userid,self.newusername, self.password)
        self.assertEqual(0, actual_result["errno"])
        self.assertEqual(self.newusername, actual_result.get("data").get("username"))

    def test03_search_user(self):
        actual_result = self.user.user_search()
        self.assertEqual(0, actual_result["errno"])
        self.assertEqual(self.newusername, actual_result.get("data").get("list")[0].get("username"))

    def test04_delete_user(self):
        actual_result=self.user.user_delete(TestUserManager.userid,self.newusername)
        self.assertEqual(0, actual_result["errno"])

if __name__ == '__main__':
        unittest.main()