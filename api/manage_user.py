from api.base import Base
from loguru import logger

class UserManager(Base):
    def __init__(self):
        self.add_user_path=self.get_url("/admin/admin/create")
        self.delete_user_path=self.get_url("/admin/admin/delete")
        self.edit_user_path=self.get_url("/admin/admin/update")
        self.search_user_path=self.get_url("/admin/admin/list?page=1&limit=20&sort=add_time&order=desc")
    def user_add(self,username,password,**kwargs):
        user_data={"username":username,"password":password}
        if kwargs:
            logger.info("添加用户的可选参数：{}".format(**kwargs))
        user_data.update(**kwargs)
        return self.post(self.add_user_path,user_data)
    def user_delete(self,userid,username,**kwargs):
        user_data={"id":userid,"username":username}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("删除用户的可选参数：{}".format(**kwargs))
        return self.post(self.delete_user_path,user_data)
    def user_edit(self,userid,username,password,**kwargs):
        user_data = {"id": userid, "username": username,"password":password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("修改用户的可选参数：{}".format(**kwargs))
        return self.post(self.edit_user_path, user_data)
    def user_search(self,**kwargs):
        return self.get(self.search_user_path,**kwargs)