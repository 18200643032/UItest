# @Time : 2020/12/8 16:53 
# @modele : XiangMuPage
# @Author : zhengzhong
# @Software: PyCharm

from public import basepage
from public.log import Log
import time
logger = Log()


class XiangMuPage(basepage.Page):
    def _gongyong(self,state,number):
        logger.error(state)
        if state == "报 名":

            self.dr.click(self.index["suanfadasai"][number])

            time.sleep(10)
            self.dr.click(self.index["suanfadasai"]["saiti_1_baomin_gouxuan"])
            logger.error(self.index["suanfadasai"]["tijiao"])
            self.dr.click(self.index["suanfadasai"]["tijiao"])

            try:
                code = self.dr.element_wait(self.index["suanfadasai"]["duanyan1"])
                logger.error("................%s"%code)
                return bool(code)

            except Exception as e:
                logger.info("元素找不到")
                return False
        elif state == "创建实例":
            self.dr.click(self.index["suanfadasai"][number])
            self.dr.click(self.index["suanfadasai"]["chuangjianshili"])
            self.dr.click(self.index["suanfadasai"]["xuanzhekuangjia"])
            self.dr.click(self.index["suanfadasai"]["tijiao"])
            time.sleep(5)
            try:
                code = self.dr.element_wait(self.index["suanfadasai"]["duanyan2"])
                return bool(code)
            except Exception as e:
                logger.info("元素找不到")
                return False

        elif state == "进入实例":
            self.dr.click(self.index["suanfadasai"][number])
            try:
                code = self.dr.element_wait(self.index["suanfadasai"]["duanyan4"])
                return bool(code)
            except Exception as e:
                logger.info("元素找不到")
                return False
        else:
            logger.info("无法报名--，报名已截至，请切换项目")
            return True

    def clike_suanfadaisai(self):
        """点击项目"""
        logger.info("点击算法大赛中------------->")
        self.dr.click(self.index["index"]["suanfadasai"])



    def clike_saiti1(self):
        """点击第一个赛题"""
        logger.info("点击第一个赛题中------------->")
        self.dr.click(self.index["suanfadasai"]["saiti_1"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["saiti_1_shujuji"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_saiti1_baoming(self):
        """点击赛题后点击报名"""
        logger.info("点击报名中------------->")
        state = self.dr.get_element(self.index["suanfadasai"]["saiti_1_baomin"]).text
        code = self._gongyong(state,"saiti_1_baomin")
        return code

    def clike_saiti2(self):
        """点击第二个赛题"""
        logger.info("点击第一个赛题中------------->")
        self.dr.click(self.index["suanfadasai"]["saiti_2"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["saiti_1_shujuji"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_saiti2_baoming(self):
        """点击赛题后点击报名"""
        logger.info("点击报名中------------->")
        state = self.dr.get_element(self.index["suanfadasai"]["saiti_2_baomin"]).text
        code = self._gongyong(state,"saiti_2_baomin")
        return code

    def clike_saiti3(self):
        """点击第三个赛题"""
        logger.info("点击第一个赛题中------------->")
        self.dr.click(self.index["suanfadasai"]["saiti_3"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["saiti_1_shujuji"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_saiti3_baoming(self):
        """点击赛题后点击报名"""
        logger.info("点击报名中------------->")
        state = self.dr.get_element(self.index["suanfadasai"]["saiti_3_baomin"]).text
        code = self._gongyong(state,"saiti_3_baomin")
        return code

    def clike_saiti4(self):
        """点击第四个赛题"""
        logger.info("点击第一个赛题中------------->")
        self.dr.click(self.index["suanfadasai"]["saiti_4"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["saiti_1_shujuji"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_saiti4_baoming(self):
        """点击赛题后点击报名"""
        logger.info("点击报名中------------->")
        state = self.dr.get_element(self.index["suanfadasai"]["saiti_4_baomin"]).text
        code = self._gongyong(state,"saiti_4_baomin")
        return code

    def clike_saiti5(self):
        """点击第五个赛题"""
        logger.info("点击第一个赛题中------------->")
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["saiti_1_shujuji"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False

    def clike_saiti5_baoming(self):
        """点击赛题后点击报名"""
        logger.info("点击报名中------------->")
        state = self.dr.get_element(self.index["suanfadasai"]["saiti_5_baomin"]).text
        code = self._gongyong(state,"saiti_5_baomin")
        return code


    def clike_saiti1_saizhi(self):
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_saizhi"])
            #base

    def clike_saiti1_saiti(self):
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_saiti"])
        #des

    def clike_saiti1_shujuji(self):
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_shujuji"])
        #dataset
    def clike_saiti1_paihangbang(self):
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_paihangbang"])
        #rank

    def clike_sait1_shujuji_zhankai(self):
        self.dr.click(self.index["suanfadasai"]["saiti_5"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_shujuji"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_shujuji_zhankai"])
        self.dr.click(self.index["suanfadasai"]["saiti_1_shujuji_zhankai_one"])
        try:
            code = self.dr.element_wait(self.index["suanfadasai"]["duanyan5"])
            return bool(code)
        except Exception as e:
            logger.info("元素找不到")
            return False


    def clike_xiayiye(self):
        """点击下一页"""
        logger.info("点击下一页中------------->")
        try:
            self.dr.click(self.index["suanfadasai"]["xiayiye"])
            return True
        except Exception as e:
            return False
    def return_alert(self):
        return self.dr.switch_to_alert()

    def return_url(self):
        """返回该页面的url"""
        return self.dr.get_url()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    def return_yunma(self):
        """返回该页面源码"""
        return self.dr.get_yuanma()
