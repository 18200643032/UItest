# # @Time : 2020/12/9 9:57
# # @modele : test_kaifahuanjing
# # @Author : zhengzhong
# # @Software: PyCharm
# import time
# from public.pages import SuanFaDaSaiPage
# from public import mytest
# class Test_Index(mytest.Login):
#     def _echom(self):
#         self.nanyou = SuanFaDaSaiPage.SuanFaDaSaiPage(self.dr)
#         self.nanyou.clike_suanfadaisai()
#         time.sleep(1)
#     def test_1(self):
#         self._echom()
#         self.assertEqual("https://developer.aiebuy.cn/race",self.nanyou.return_url())