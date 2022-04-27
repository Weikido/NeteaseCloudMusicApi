# version 0.2
# Date: 2022-04-22
#   - 封装 获取喜欢音乐列表
#   - 封装 喜欢或取消喜欢音乐
#   - 封装部分API功能
# version 0.1
# Date: 2022-04-22
#   - 初始化模板

import requests


class NeteaseCloudMusicApi:

    # #### 初始化API类开始 ### #
    def __init__(self, base_url, headers=None):
        """
        初始化 NeteaseCloudMusicApi 基本参数
        :param base_url: 网站基础地址, 如: http://localhost:3000/
        :param headers: 请求头. 不填默认为: {'User-Agent': 'None'}
        """

        if headers is None:
            headers = {'User-Agent': 'None'}

        print("[*] NeteaseCloudMusicApi.init() ...")

        # 处理默认参数
        self.base_url = base_url
        self.headers = headers
        self.cookies = None

        print(f"base_url = {self.base_url}\n")

        # ### 初始化API类结束 ### #

    # ### 常用API接口封装开始 ### #
    def ping(self):
        """
        测试API是否连通
        :return: 测试结果
        """
        print("[*] NeteaseCloudMusicApi.ping() ...")
        response = requests.get(self.base_url, headers=self.headers)
        print(response)
        return response

    def get_login_cookies(self, email, password):
        """
        通过邮箱密码获取登录cookies
        :param email: 163 网易邮箱
        :param password: 密码
        :return: cookies
        """
        print(f"[*] NeteaseCloudMusicApi.get_login_cookies({email}) ...")
        response = 'Wrong email or password'
        try:
            response = requests.get(self.base_url + 'login' + '?email=' + email + '&password=' + password,
                                    headers=self.headers)
            print(response)
            print(response.json())
            if response.json()["cookie"]:
                print(response.json()["cookie"])
                # return response.json()["cookie"]
                self.cookies = response.cookies
                return response.cookies
        except:
            print(response)
            print(f"[*] NeteaseCloudMusicApi.get_login_cookies({email}) failed.")
            return False

    def get_like_list(self, cookies, uid):
        """
        调用此接口 , 传入用户 id, 可获取已喜欢音乐 id 列表(id 数组)
        :param uid: 用户 id
        :return: 已喜欢音乐 id 列表(id 数组)
        """
        print(f"[*] NeteaseCloudMusicApi.get_like_list({uid}) ...")

        url = self.base_url + 'likelist'
        params = {
            'uid': uid,
        }
        response = requests.post(url=url, params=params, cookies=cookies, headers=self.headers)
        print(response)
        res_data = response.json()


        return res_data, len(res_data["ids"])

    def do_like_or_dislike(self, cookies, id, like):
        """
        调用此接口 , 传入音乐 id, 可喜欢或取消喜欢该音乐
        :param cookies: 登录后的 cookies
        :param id: 歌曲 id
        :param like: 布尔值 , 默认为 true 即喜欢 , 若传 false, 则取消喜欢
        :return:
        """
        print(f"[*] NeteaseCloudMusicApi.do_like_or_dislike(id={id}, like={like}) ...")
        response = 'Wrong response'
        url = self.base_url + "like"
        params = {
            'id': id,
            'like': like
        }
        try:
            response = requests.get(url=url, params=params, cookies=cookies, headers=self.headers)
            print(response.json())
            if response.json()["code"] == 200:
                return True
        except:
            print(response)
            print(f"[*] NeteaseCloudMusicApi.do_like_or_dislike({id}={like}) failed.")
            return False

    # ### 常用API接口封装结束 ### #
