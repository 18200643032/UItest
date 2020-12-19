# @Time : 2020/12/11 11:28 
# @modele : LoginPage
# @Author : zhengzhong
# @Software: PyCharm

from public import basepage
from public.log import Log

logger = Log()
class LoginPage(basepage.Page):
    def into_nanyoulogin_page(self):
        """打开南邮登录页"""
        logger.info("打开南邮登录页中------------->")
        self.dr.open(self.index["login"]["url"])

    def input_usernam_password(self,username,password):
        logger.info("输入账号密码中------------->")
        self.dr.send_key(self.index["login"]["login_username"],username)
        self.dr.send_key(self.index["login"]["login_password"],password)
        self.dr.click(self.index["login"]["login_sumbit"])

    def return_url(self):
        """返回该页面的url"""
        return self.dr.get_url()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    def return_yuanma(self):
        """返回该页面的源码"""
        return self.dr.get_yuanma()