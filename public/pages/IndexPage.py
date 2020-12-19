from public import basepage
from public.log import Log

logger = Log()


class IndexPage(basepage.Page):

    def into_baidu_page(self):
        """打开南邮首页"""
        logger.info("打开首页中------------->")
        self.dr.open(self.index["index"]["url"])
    def clike_search_login_you1(self):
        """点击登录右上"""
        logger.info("点击登陆中------------->")
        self.dr.click(self.index["index"]["youshang_login"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan1"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_register_you1(self):
        """点击注册右上"""
        logger.info("点击注册中------------->")
        self.dr.click(self.index["index"]["youshang_zhuci"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan2"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_search_login_you_zhong1(self):
        """点击登录右中"""
        logger.info("点击登陆中------------->")
        self.dr.click(self.index["index"]["zhong_login"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan1"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_register_you_zhong1(self):
        """点击注册右中"""
        logger.info("点击注册中------------->")
        self.dr.click(self.index["index"]["zhong_zhuci"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan2"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_register_you_xia1(self):
        """点击注册下"""
        logger.info("点击注册中------------->")
        self.dr.click(self.index["index"]["youxia_zhuci"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan2"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_images1(self):
        """点击图片1"""
        logger.info("点击图片1中------------->")
        self.dr.click(self.index["index"]["zhong_img1"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan4"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_images2(self):
        """点击图片2"""
        logger.info("点击图片2中------------->")
        self.dr.click(self.index["index"]["zhong_img2"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan4"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def clike_search_images3(self):
        """点击图片3"""
        logger.info("点击图片3中------------->")
        self.dr.click(self.index["index"]["zhong_img3"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan4"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def go_personal(self):
        logger.info("点击个人中心------------->")
        self.dr.click(self.index["index"]["go_gerenzhongxin"])
        try:
            code = self.dr.element_wait(self.index["index"]["duanyan5"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False
    def return_url(self):
        """返回该页面的url"""
        return self.dr.get_url()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

