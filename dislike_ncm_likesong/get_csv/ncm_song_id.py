# Date: 2022-04-26
#   - 功能
#       - 根据网易云我喜欢列表歌曲歌名和QQ音乐我喜欢列表歌曲歌名对比,获取重复喜欢列表歌曲的id
#       - 因技术有限,获取歌曲id有重复,去重获得delete_song_norepeat.csv
#   - 提示 如需多次运行本文件,请注释掉获取delete_song_id.csv部分,或者手动清除delete_song_id.csv内容,不然delete_song_id.csv会一直增加相同内容

"""
1467971656,想在夏日撞见你
1914116947,你有多久没有抬起头认真地数过星星
1411542710,小事
"""
song_dict = {}
# 以utf-8格式读取ncmlike_list.csv文件 获取songid和songname
with open('ncmlike_list.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(',')
        song_id = line[0]
        song_name = line[1]
        # print(song_id, song_name)
        #将歌曲id和歌曲名称对应到字典
        song_dict[song_id] = song_name
    # print(song_dict)
# print(song_dict['1467971656'])

# 以utf-8格式读取qqlike_list.csv文件 获取歌曲名称
with open('qqlike_list.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(',')
        qqsong_name = line[0]
        # print(qqsong_name)

        # 将song_dict中song_name与qqsong_name进行比较 如果qqsong_name包含song_name则获取歌名id
        for song_id in song_dict:
            if song_dict[song_id] in qqsong_name:
                # print(song_dict[song_id],song_id)
                #将song_dict[song_id],song_id写入delete_song_id.csv文件
                # with open('delete_song_id.csv', 'a', encoding='utf-8') as f:
                #     f.write(song_id + ',' + song_dict[song_id] + '\n')
                # 将song_id写入delete_song_id.csv文件
                with open('delete_song_id.csv', 'a', encoding='utf-8') as f:
                    f.write(song_id + '\n')

# 把delete_song_id.csv传给ids
# 以utf-8格式读取delete_song_id.csv文件 获取歌曲id
ids = []
with open('delete_song_id.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        # 将歌曲id写入ids
        ids.append(line)

        # 这里可以检测获取delete_song_norepeat.csv中id数量是否正确
        # print(ids)
        # # 统计ids中的歌曲数量
        # print(len(ids))
        # # 统计ids的不重复项目
        # print(len(set(ids)))

        # 删除ids中的重复项目
        ids = list(set(ids))
    print(ids)
    # 将ids写入delete_song_norepeat.csv文件
    with open('delete_song_norepeat.csv', 'a', encoding='utf-8') as f:
        for id in ids:
            f.write(id + '\n')





