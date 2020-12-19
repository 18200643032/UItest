from public import basepage
from public.log import Log

logger = Log()


class RegisterPage(basepage.Page):

    def into_register_page(self):
        """打开南邮注册页"""
        logger.info("打开首页中------------->")
        self.dr.open(self.index["index"]["url"])
    def input_send_key(self):
        """输入内容"""
        logger.info("打开首页中------------->")
        self.dr.send_key(self.index["index"]["xxx"])
        """-----------------------------"""

    def sumbit(self):
        """提交"""
        logger.info("打开首页中------------->")
        self.dr.click(self.index["index"]["xxx"])

    def return_alert(self):
        return self.dr.switch_to_alert()

    def return_url(self):
        """返回该页面的url"""
        return self.dr.get_url()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    def return_yuanma(self):
        """返回该页面的源码"""
        return self.dr.get_yuanma()
#
