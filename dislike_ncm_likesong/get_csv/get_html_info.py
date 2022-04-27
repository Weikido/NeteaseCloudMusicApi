# Date: 2022-04-26
#   - 功能 根据网页的html信息,获取网易云音乐我喜欢列表歌曲的id和对应歌名
#   - 步骤
#        - 获取like_list.html后,先用VS Code的HTML格式化插件,把HTML格式化
#        - 根据每首歌所对应的唯一<a href="/song?id=1467971656">和<b title="想在夏日撞见你">,获取我喜欢列表歌曲的id和对应歌名

import re

from bs4 import BeautifulSoup


def get_html_info():
    """
    获取网页信息
            <tr id="14679716561650638993093" class="even ">
            <td class="left">
                <div class="hd "><span data-res-id="1467971656" data-res-type="18" data-res-action="play"
                        data-res-from="13" data-res-data="372325599" class="ply ">&nbsp;</span><span
                        class="num">1</span></div>
            </td>
            <td class="">
                <div class="f-cb">
                    <div class="tt">
                        <div class="ttc"><span class="txt"><a href="/song?id=1467971656"><b title="想在夏日撞见你">想在夏<div
                                            class="soil">鷶</div>日撞见你</b></a></span></div>
                    </div>
                </div>
            </td>
            <td class=" s-fc3"><span class="u-dur candel">03:23</span>
                <div class="opt hshow"><a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表"
                        hidefocus="true" data-res-type="18" data-res-id="1467971656" data-res-action="addto"
                        data-res-from="13" data-res-data="372325599"></a><span data-res-id="1467971656"
                        data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span><span
                        data-res-id="1467971656" data-res-type="18" data-res-action="share" data-res-name="想在夏日撞见你"
                        data-res-author="囍浪"
                        data-res-pic="http://p4.music.126.net/itkZc3tF8dLvoQi7EEK-wg==/109951165200009241.jpg"
                        class="icn icn-share" title="分享">分享</span><span data-res-id="1467971656" data-res-type="18"
                        data-res-action="download" class="icn icn-dl" title="下载"></span><span data-res-id="1467971656"
                        data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span></div>
            </td>
            <td class="">
                <div class="text" title="囍浪"><span title="囍浪"><a class="" href="/artist?id=35653445" hidefocus="true">囍
                            <div class="soil">鑰堯儯徔</div>浪</a></span></div>
            </td>
            <td class="">
                <div class="text"><a href="/album?id=93395021" title="自恋日记">自恋<div class="soil">着组备</div>日记</a></div>
            </td>
        </tr>
    :return:
    """
    with open("./like_list.html", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")
        # print(soup.prettify())
        # 使用正则表达式获取/song?id的值
        pattern = re.compile(r"/song\?id=(\d+)")
        # 获取所有的data-res-id的值
        res_ids = re.findall(pattern, content)
        print(res_ids)
        # 使用正则表达式获取data-res-name的值
        pattern = re.compile(r'data-res-name="(.*?)"')
        # 获取所有的data-res-name的值
        res_names = re.findall(pattern, content)
        print(res_names)

        # 将歌曲id和歌曲名称写入csv文件
        with open("./ncmlike_list.csv", "w", encoding="utf-8") as f:
            for id, name in zip(res_ids, res_names):
                f.write(id + "," + name + "\n")


if __name__ == "__main__":
    get_html_info()
