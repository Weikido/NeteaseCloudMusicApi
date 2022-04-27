# version 0.2
# Date: 2022-04-22
#   - 封装 获取喜欢音乐列表
#   - 封装 喜欢或取消喜欢音乐
#   - 封装部分API功能
# version 0.1
# Date: 2022-04-22
#   - 初始化模板


from ncm_api import NeteaseCloudMusicApi


class NeteaseCloudMusicFuc:
    def __init__(self, base_url, headers=None):
        """
        初始化 NeteaseCloudMusicFuc 基本参数
        :param base_url: 网站地址. 仅基本地址, 如: example.com / abc.example.com
        :param headers: 请求头. 不填默认为: {'User-Agent': 'None'}
        """
        if headers is None:
            headers = {'User-Agent': 'None'}

        print("[*] NeteaseCloudMusicFuc.init() ...")
        self.base_url = base_url
        self.headers = headers

        self.ncm_api = NeteaseCloudMusicApi(base_url=self.base_url)

    def ping(self):
        """
        测试网络是否通畅
        :return:
        """
        print("[*] NeteaseCloudMusicFuc.ping() ...")
        return self.ncm_api.ping()

    def get_login_cookies(self, email, password):
        """
        通过邮箱密码获取登录cookies
        :param email: 163 网易邮箱
        :param password: 密码
        :return:
        """
        print(f"[*] NeteaseCloudMusicFuc.get_login_cookies({email}) ...")
        login_cookies = self.ncm_api.get_login_cookies(email=email, password=password)
        return login_cookies

    def get_like_list(self, cookies, uid):
        """
        调用此接口 , 传入用户 id, 可获取已喜欢音乐 id 列表(id 数组)
        :param cookies: 登录后的 cookies
        :param uid: 用户 id
        :return: 已喜欢音乐 id 列表(id 数组)
        """
        print(f"[*] NeteaseCloudMusicFuc.get_like_list({uid}) ...")
        return self.ncm_api.get_like_list(cookies, uid=uid)

    def do_dislike(self, cookies, id):
        """
        取消喜欢音乐
        :param cookies: 登录后的 cookies
        :param id: 音乐 id
        :return:
        """
        print(f"[*] NeteaseCloudMusicFuc.do_dislike({id}) ...")
        if self.ncm_api.do_like_or_dislike(cookies, id=id, like='false'):
            print(f"[*] NeteaseCloudMusicFuc.do_dislike({id}) success")
            return True
        else:
            print(f"[*] NeteaseCloudMusicFuc.do_dislike({id}) failed")
            return False
