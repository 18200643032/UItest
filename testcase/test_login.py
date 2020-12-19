# # @Time : 2020/12/11 11:28
# # @modele : test_login
# # @Author : zhengzhong
# # @Software: PyCharm
#
# from public.pages import LoginPage
# from public import mytest
#
# class Test_Login(mytest.MyTest):
#
#     def test_1(self):
#         """正确的"""
#         nanyou = LoginPage.LoginPage(self.dr)
#         nanyou.into_nanyoulogin_page()
#         nanyou.input_usernam_password("zz66","123456")
#         self.assertIn("zz66",nanyou.return_yuanma())
#
#     def test_2(self):
#         """错误的用户名"""
#         nanyou = LoginPage.LoginPage(self.dr)
#         nanyou.into_nanyoulogin_page()
#         nanyou.input_usernam_password("zz616", "123456")
#         self.assertIn("zz616", nanyou.return_yuanma())
#
#     def test_3(self):
#         """错误的密码"""
#         nanyou = LoginPage.LoginPage(self.dr)
#         nanyou.into_nanyoulogin_page()
#         nanyou.input_usernam_password("zz66", "1234567")
#         self.assertIn("zz66", nanyou.return_yuanma())
#     def test_4(self):
#         """错误的用户名"""
#         nanyou = LoginPage.LoginPage(self.dr)
#         nanyou.into_nanyoulogin_page()
#         nanyou.input_usernam_password("zz6@6", "123456")
#         self.assertIn("zz6@6", nanyou.return_yuanma())