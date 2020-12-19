# @Time : 2020/12/8 16:36
# @modele : test_suanfadasai
# @Author : zhengzhong
# @Software: PyCharm
from public.pages import SuanFaDaSaiPage
from public import mytest
import time

class Test_Index(mytest.Login):
    def _echom(self):
        self.nanyou = SuanFaDaSaiPage.SuanFaDaSaiPage(self.dr)
        self.nanyou.clike_suanfadaisai()
        time.sleep(1)
    def test_1(self):
        self._echom()
        self.assertEqual("https://developer.aiebuy.cn/race",self.nanyou.return_url())

    def test_2(self):
        self._echom()
        code = self.nanyou.clike_xingrenchongshibie()
        self.assertTrue(code)
    def test_3(self):
        self._echom()
        code = self.nanyou.clike_arfuzhu()
        self.assertTrue(code)

    def test_4_1(self):
        self._echom()
        code = self.nanyou.clike_saiti1()
        self.assertTrue(code)

    def test_4_2(self):
        self._echom()
        code = self.nanyou.clike_saiti1_baoming()
        self.assertTrue(code)
    def test_5_1(self):
        self._echom()
        code = self.nanyou.clike_saiti2()
        self.assertTrue(code)
    def test_5_2(self):
        self._echom()
        code = self.nanyou.clike_saiti2_baoming()
        self.assertTrue(code)

    def test_6_1(self):
        self._echom()
        code = self.nanyou.clike_saiti3()
        self.assertTrue(code)
    def test_6_2(self):
        self._echom()
        code = self.nanyou.clike_saiti3_baoming()
        self.assertTrue(code)
    def test_7_1(self):
        self._echom()
        code = self.nanyou.clike_saiti4()
        self.assertTrue(code)
    def test_7_2(self):
        self._echom()
        code = self.nanyou.clike_saiti4_baoming()
        self.assertTrue(code)

    def test_8_1(self):
        self._echom()
        code = self.nanyou.clike_saiti5()
        self.assertTrue(code)
    def test_8_2(self):
        self._echom()
        code = self.nanyou.clike_saiti5_baoming()
        self.assertTrue(code)

    def test_9(self):
        self._echom()
        self.nanyou.clike_saiti1_saizhi()
        self.assertIn("base",self.nanyou.return_url())
    def test_10(self):
        self._echom()
        self.nanyou.clike_saiti1_saiti()
        self.assertIn("des",self.nanyou.return_url())
    def test_11(self):
        self._echom()
        self.nanyou.clike_saiti1_paihangbang()
        self.assertIn("rank",self.nanyou.return_url())

    def test_12(self):
        self._echom()
        code = self.nanyou.clike_sait1_shujuji_zhankai()
        self.assertTrue(code)




