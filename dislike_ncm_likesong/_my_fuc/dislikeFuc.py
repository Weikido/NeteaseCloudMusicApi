# version 0.3
# Date: 2022-04-26
#   - 读取delete_song_id.csv文件 获取歌曲id并取消喜欢
#   - 取消喜欢失败并重试
# version 0.2
# Date: 2022-04-22
#   - 根据歌曲id取消喜欢音乐
# version 0.1
# Date: 2022-04-22
#   - 初始化模板

import time

from ncm_fuc import NeteaseCloudMusicFuc

# ###### 全局变量配置 ###### #

# ### 接口请求地址 ### #
base_url = 'http://localhost:3000/'

# ### 网易云音乐 用户ID ### #
uid = 'XXX'

# ### 网易云音乐 Cookie ### #
cookies = {
     '__remember_me': 'true',
    'NMTID': '00OccQZINTn3z5vn0gcihEZCqr_TzoAAAGAZhwNCA',
    'MUSIC_U': '154c4268bee57a34afa84b741fb17aa60f50b79ae78fdcd71f021f958c43528e993166e004087dd3cbf09c25dba672dda842e7a8e3dc18aafd57581773fb0e339bb192f7a7cc78eea89fe7c55eac81f3',
    '__csrf': '2ccaa0c4950c9fb3048234f1018c97fa',
}

# 注: Cookies 手动获取方式
# 1. 邮箱密码方式 :   http://localhost:3000/login?email=xxxxx&password=yyyyy  // 这里填邮箱和密码
# 2. 手机号密码方式 :   http://localhost:3000/login/cellphone?phone=xxx&password=yyy    // 这里填手机号和密码
# 因为是跨域请求, 直接手动传入 cookie, 否则会因为没带上 cookie 导致 301
# 具体例子可看 public/test.html, 访问http://localhost:3000/test.html(默认端口的话) 例子使用 jQuery 和 axios

# 其余具体说明见本项目 README.md

# ###### 全局变量配置结束 ###### #


# 初始化API接口类
ncm_fuc = NeteaseCloudMusicFuc(base_url)

# 测试接口是否正常
def test_ping():
    ncm_fuc.ping()

# 此方法测试未成功
# def test_get_login_cookies():
#     cookies = ncm_fuc.get_login_cookies(email, password)
#     print(cookies)

# 获取用户喜欢歌曲ids列表
def test_get_like_list():
    ncm_fuc.get_like_list(cookies, uid)


# 取消喜欢歌曲, 通过ids批量传入
def test_do_dislike():
    # 获取用户的当前喜欢歌曲列表
    res_data, before_num = ncm_fuc.get_like_list(cookies, uid) 
    
    #把delete_song_id.csv传给ids
    # 以utf-8格式读取delete_song_id.csv文件 获取歌曲id
    ids = []
    with open('./delete_song_id.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # print(line)
            #将歌曲id写入ids
            ids.append(line)

    # 处理ids,标记为已经取消喜欢
    opt_res = False
    for id in ids:
        try_count=1
        while True:
            del_res = ncm_fuc.do_dislike(cookies, id)
            print(f"[#] 当前操作已经尝试{try_count}次, 最多尝试3次...")
            if try_count==3:
                break
            print(f"[#] 删除歌曲{id}结果: {del_res}")
            if del_res:
                opt_res = True
                break
            else:
                try_count = try_count+1
                print(f"[#] 删除歌曲{id}失败,10s后重试。。")
                time.sleep(10)
            opt_res = False

        # 这里建议time.sleep > 10秒,不然会触发系统风控,导致运行失败   
        time.sleep(12)
        continue

    # 获取喜欢歌曲列表, 并判断是否取消喜欢成功
    print("\n")
    if opt_res:
        print('取消喜欢成功...')
        while True:
            res_data, after_num = ncm_fuc.get_like_list(cookies, uid)
            if before_num == after_num:
                print('等待10s刷新操作结果...')
                time.sleep(10)
                continue
            else:
                print('成功刷新操作结果...')
                break
    else:
        print('取消喜欢失败, 请等待技能冷却后再排查bug...')

    # 打印结果
    res_data, after_num = ncm_fuc.get_like_list(cookies, uid) # 这里填用户id
    print(f"原始歌单歌曲数量: {before_num} \n"
          f"尝试删除歌曲数量: {len(ids)} \n"
          f"剩余歌单歌曲数量: {after_num} \n")


if __name__ == '__main__':
    test_ping()
    # test_get_login_cookies()
    # test_get_like_list()
    test_do_dislike()
