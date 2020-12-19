import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .log import Log
from selenium.webdriver.common.action_chains import ActionChains

logger = Log()
class PySelenium(object):
    """
    初始化浏览器
    """
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--window-size=1290x792')
        # options=chrome_options
        dr = webdriver.Chrome(options=chrome_options)
        try:
            self.driver = dr
        except Exception:
            raise NameError("没有找到浏览器")

    """日志"""
    def my_print(self,msg):
        logger.info(msg)

    """浏览器最大化"""
    def max_window(self):
        self.driver.maximize_window()
    """
    元素定位10秒.找不到报错
    """
    def element_wait(self, css, secs=10):

        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "id":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "name":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == "class":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
        elif by == "link_text":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
        elif by == "xpath":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "xpaths":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "css":
            state = WebDriverWait(self.driver, secs, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),messages)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        return state


    """
    判断元素的定位方式，并返回元素。
    """
    def get_element(self,css):
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "xpaths":
            v3 = css.split("->")[2].strip()
            element = self.driver.find_elements_by_xpath(value)[int(v3)]
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)

        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        return element


    """
    打开网页
    """
    def open(self, url):
        try:
            self.driver.get(url)
        except Exception:
            raise


    """悬浮在一个元素上"""
    def to_element(self,css):
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
        except Exception:
            raise
    """
    点击
    """
    def click(self,css):
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.click()
        except Exception:
            raise

    """
    双击元素
    """
    def two_click(self,css):
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.double_colick()
        except Exception:
            raise

    """输入内容"""
    def send_key(self,css,text):
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.clear()
            el.send_keys(text)
        except Exception:
            raise


    """刷新"""
    def F5(self):
        self.driver.refresh()

    """退出"""
    def quit(self):
        self.driver.quit()

    """浏览器后退"""
    def back(self):
        self.driver.back()


    """浏览器前进"""
    def forward(self):
        self.driver.forward()

    """提交表单"""
    def submit(self,css):
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.submit()
        except Exception:
            raise

    #获取-------------------------
    """获取文本内容"""
    def get_text(self,css):
        try:
            self.element_wait(css)
            text = self.get_element(css).text
            return text
        except Exception:
            raise

    """获取标题"""
    def get_title(self):
        title = self.driver.title
        return title
    """获取URL"""
    def get_url(self):
        url = self.driver.current_url
        return url

    """返回页面源码"""
    def get_yuanma(self):
        yuanma = self.driver.page_source
        return yuanma

    """弹出框"""
    def get_switch_to_alert(self):
        text = self.driver.switch_to.default_content()
        return text.text()
    """执行JS代码"""
    def set_js(self):
        js = "document.getElementsByClassName(\"ant-modal-wrap\")[0].style.display='block';"
        self.driver.execute_script(js)

    """截图"""
    def take_screenshot(self,file_path):
        try:
            self.driver.get_screenshot_as_file(file_path)
        except Exception:
            raise

