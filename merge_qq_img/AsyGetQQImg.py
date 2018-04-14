# coding: utf-8
import asyncio
import requests
import os
from PIL import Image
import numpy as np
from io import BytesIO
from random import randint
# QQ空间默认图片的bytes
QQZONE_ONE_BYTES = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x002\x00\x00\x002\x08\x02\x00\x00\x00\x91]\x1f\xe6\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\x03(iTXtXML:com.adobe.xmp\x00\x00\x00\x00\x00<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?> <x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.156797, 2014/08/20-09:53:02        "> <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"> <rdf:Description rdf:about="" xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/" xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmpMM:DocumentID="xmp.did:1DB54A88144811E6BE93E403352432C6" xmpMM:InstanceID="xmp.iid:1DB54A87144811E6BE93E403352432C6" xmp:CreatorTool="Adobe Photoshop CC 2014 (Macintosh)"> <xmpMM:DerivedFrom stRef:instanceID="xmp.iid:88EE9701EFFB11E5BFECDC804EDED507" stRef:documentID="xmp.did:88EE9702EFFB11E5BFECDC804EDED507"/> </rdf:Description> </rdf:RDF> </x:xmpmeta> <?xpacket end="r"?>n\xf6\xa9\xc1\x00\x00\x040IDATx\xda\xec\x98\xd9R\xe3@\x0cE\x89\'a\x0b\x10\x18\xd6\x07\xfe\xff\xd3(\xa0\x08\xfb20Y\xe6\x94\xcfD\xd5\xd8YL\xe2b2U\xe9\x07W\xbb\xdd\x96\xae\xae\xd4\x92\xec\xc6\xcb\xcb\xcb\xda\xf2\x8dlm)\xc7\n\xd6\n\xd6\xdf1\x1c\x0e\x7f\xe4c\xb9`5\x9b\xcd_\xf9\xa8\x0bY\r\xb0\xb2,\x83\xad\xab\xab\xab\xcb\xcbK&\xdc.\x05,\xa8z||\x1c\x0c\x06`zxx\xa8\x85\xb0Ea\x01\xe2\xfd\xfd\x1dX\xc6\x16\x93\x8f\x8f\x8f\xc5\x91e\x8b{\xf0\xe9\xe9\xa9\xd7\xebe\xf9\xe8\xf7\xfb [\xdc\x8f\xd9\x82T\x11\xe6\xc0\xc2\x8f\xa9C\xdf\xde\xdeb\xe5\x1f\xc0\x82\x15\x82\t\xaa\x1a\x8d\x86+L\x880\x90\xc5\xcaw\xc3\x82\x0fX\xa1\xd2\xb7Z\xadt\x9d[\x16___\x0b\xeb\xdf\x04\x0bV\xee\xef\xefe\xa8\xfc\x14\x169\x9bss6\',\x98\x80\x8fI1\xc4"O\x9f\x9f\x9f\xe7\x8e\xb0\xaa\xaf5>\x0fN\x1c|\xcc\x0c\xbbv\xbb\x8d\x01\xc3\xcf\xa3\x92\xba\xb1m\xa0\xe4#Z\x10\xc8\xea\xe7\xa37\x1a\xe4*\xf2\x93\x89@M\xa9>\xdf\xc2\x89\xeb\xeb\xeb\x1b\x1b\x1b\xcd|pl\xbd*p:\xd01\xb0\xcc@\xe8\x16\xc7\xef\xd1\xe0\xd6T\xae \xa5k\x00Wm`\xee\x1e\xaeb\r\x0b\x19`j\x8dF\x00\xd5\xe6\x19Nd+\x11c,\x03E\xe9\xa9b\xb5*\x172\x98\x98\xdf\xd3\x14\x8a\x1a-!\xabE\xd2\xe7-\xe6\xd0\x1c\xc6#\x01\x818zoo\xaf\x80l|lA!\xaf\xa9;=z\\\xdb\xf9\xc05\x02r]z\x9c\xa0\x89G[[[2G\xec\xdf\xde\xdejXZ\x94\xd8\tD\xd0\xec\xee\xee\xce\x0ey\xf6moo\x9f\x9f\x9f\xd3\x11 4\x15\xc4\xed\xfe\xfe\xbe\x96\xe1\\L\x0fo\xea#l\xb0\xfe\xc8\xb1.\x1b\x9b#<4l>;;\xc3Hx\xad\x14\xf2x\x87u\x1a\x95\x82\x89\xcc\x81\x02\xa64\xc6\r\xf0pe\xa7\xd3\x01\x8d>\xbd\xb9\xb9!\xe3\xeb\xacT>\xb8\x81uzz\nU\x98W5o\xb1\x15\xceNNN"x\x1d\x98e\xa9\t\x1c\x9e,\x1e\xd9GH0\xb0\x90pqq1\x05\x13\xc2\'a\x9a\x96\xb7@\xc0kH\xc4\x9bFh\\\xcb\x1ea3\xea\xd1tpp\x80\xd6\xbb\xbb;\xe2\x89I\xb9\xfex\xee\x8e\x8e\x8e\x08\x86I\x98f\xa4S^\xdb\xd9\xd9A\xfa\xf5\xf5\xf5$L\xa8\x01\x13\xf1qxx\xc8\x95\xa3\xd7\xedv\xe9)\xd8L$\x14r\x92\x9b\xc1\x84\xa3\xa7`\x9a\x9d\xe5y\x19\xb3\x98\x8cE\xa6C\x01\x04I\xdcJ\x12\x8a%i,&7\x97c\xfc\xcb\xc5Gd\x08\x05\x99g-\xbc\x8czL\x87$\x18%\xdb\xe1n\x1c\xc4\x1e\xbb\xc2\xa8\x16&^\xf6\xff\xcc\x07\x93\x99%\xa8Q\xf1\x1f\x04\x08\xa8q\xf0\x81>@\xa0\x18\xff\x82\t\x10\x9a\xee\xe1\xb0(\x99N\xd3d\xc6\x04\x92\x8e\x8f\x8fM.\xb5\x95j\xc4\xc1\x19\x94\xd0\x17\x80L_\xa0,\xdc\x01%V\xc0\x88\xeb\xb4\n\xf1\nG\x1b\xd0\x84\x1d\x13\x8cL\x0f\xf8\xfc\xb0\x8c$\x1d\x87\xd18\x8e\xdb\x82\xe8\xb85\xde\xc3}\xe6^\xb2 \x9e\xe1t[\x07\xeba\xcb`B:Y\xc0\xb3\x8dJKS\xe8\x88\x8e \xfc\xe8\xb0\xe9\x00\xb4\x1c3\xaf\r\x96!\x05\x14"\x8c2\x17=O\xda\xd8\x0cF\xc3.(\xbaS7c\x0f\xb5+JVml\x19\xaazdR\x8b\x96\xf6ji\xd5\x92-\xa3\xad\xce\xeeT\'F\xe74G\x1f\\\x91\xa7/\xc0\xb2\xcd\xc2/\x93>\x19\xa2~\x97+`\xda2\xe8\xd6*\xe0\xb2\xea\xb0`\xab\xac\xd2<\xc9\xd3N>\xe2\xb6,\xc1v\xb7\xe2\xb7PU\xb6\x8c\xe2T\xa8\xfc\xe1P\xce<\xa9\x95\x94a\x93Hb#\x11\x00.mYCB\xc5o\xa1\xaa\xb0\x8cY\x85\n\x08\xadd\n0mnn\x9a\x14xD:\xa5/e\xb1\x00NX\x08as\x9d!o\xbc\x0b\x88\x8c*C\x80H\x13\xbd\xc5\x80A.\xb5M\xa0\xdf\np!\xa4NX~,P7P\x86\xa7P\\\x00T\xa8T\xd2I\xfe\x84Q\x98\xa3\xe6\xf8\xbb0R\x7f\r\xb0@\x00\xf9\x90dC<\x05P\x19\x1c\x1e$\xb3C\xad\xffK\xa6\x97\xc2/w\x10\x86H|>\xcc\xf1o\x07\t\xc6@\x9dN\xd4\xf4\xb9\xff\xa3\x98\xe2W\xff\xe5W\xb0V\xb0\xfe/X\x7f\x04\x18\x00\x1d\xa0\x1c\xb1\x0fZ\x81\x08\x00\x00\x00\x00IEND\xaeB`\x82'
QQZONE_TWO_BYTES = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x00\x00d\x00d\x00\x00\xff\xec\x00\x11Ducky\x00\x01\x00\x04\x00\x00\x00P\x00\x00\xff\xee\x00\x0eAdobe\x00d\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x02\x02\x02\x03\x04\x03\x02\x02\x03\x04\x05\x04\x04\x04\x04\x04\x05\x06\x05\x05\x05\x05\x05\x05\x06\x06\x07\x07\x08\x07\x07\x06\t\t\n\n\t\t\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x01\x03\x03\x03\x05\x04\x05\t\x06\x06\t\r\x0b\t\x0b\r\x0f\x0e\x0e\x0e\x0e\x0f\x0f\x0c\x0c\x0c\x0c\x0c\x0f\x0f\x0c\x0c\x0c\x0c\x0c\x0c\x0f\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\xff\xc0\x00\x11\x08\x002\x002\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x7f\x00\x01\x00\x02\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x06\x01\x02\x04\x07\x03\t\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x02\x03\x05\x01\x10\x00\x02\x01\x03\x02\x04\x02\x08\x07\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x00\x11\x04\x12\x05!1\x13\x06A\xb1Qaq\x812r#\x14\x91\xa1\xc1\xd1"Rb\x15\x11\x00\x02\x02\x02\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x11\x021\x03!\x12\x04\x14Q"\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfd\x86\xaf\\\xf2\xc5\x01\xba#\xc8\xe9\x1cj]\xdc\x85D\x1cI\'\x80\x02\x8d\xc0JL\xc9\x1b\xc3#\xc5*\x94\x922U\xd0\xf3\x04s\x14NCP|\xe8\x05\x00\xa0\x14\x02\x80\xb7v\x96\xdf\xf7\x19o\x9b"\xde<N\x11\xdf\xc6F\xfd\x87\xe9Szo\n?J<\xf4\x97?\x86\xfd\xdf\x81\xd2\xc9\x8b=\x16\xc9\x924K\xf3\xa8\xe1\xf8\x8f*y\xaf*\x07\xa2\x90\xe4\xa7U$\xe2\x80P\x12[^\x14\x19\xf9C\x1a|\xb1\x89\xac}7+\xabS_\xe1\xe6-z\xc6\xcb:\xa9JM\xd2\xaa\xce\x1b\x82\xe4\xbd\x9f\x81\x18\xd56VD\x96\xe7\xd3\x00~AX\xd4\xbfM\x9e\x12(\xf9\xd2\xcb%\xf1[\x1bk\xc7\\l|<\xb3\x12\x92\xda\x84L\xc4\x93\xcc\x9a\xe5i\xbb\x96\xd1\xd2\xb1E\t3\x87r\xddv\x8c\xa8[\x0bpL\x9cu\x92\xc4k\x89\x91\x81\x07\x98\xb8>U\xbdz\xee\x9c\xd6\x0c\xdfeZ\x87\' \xed\x0c\t\xa3Y \xcb\xc8Dqt\xea(\xbf\xbc\x15SZ\xfal\xb2\x91\x9f\x9e\xaf\x0c\xa9n\xd8\x10m\xd9?m\x0eX\xcbe\x1fV\xcb\xa7A\xfe\xa7\x89\xb9\xaau\xdd\xddKPO\xb2\x8a\xae$\x8a\xae\x86\x0c\xd0\x1e\x81\xdb{\xf4\xb9\x0f\x1e\xdd\x97\xaaYH?o\x91\xe2B\x82l\xfe\xe1\xce\xa3\xdf\xa5/\xe9\x15\xe9\xda\xdf\xf2\xc9\x1d\xc7\xb8!\x82Q\x85\x82c\x9f1\xce\x9dn\xc1b\x8c\xff\x00\xa6$\x03oEs\xa6\x96\xd4\xbc\x1b\xbe\xd4\x9c,\x99\xdb\xf6\xfcU\x97\xefssc\xdcw\x06\xfe]R\xc0\xa2|\x8b\xe1oO\x95/w\x10\x94!J)\x96\xe5\x9c]\xc5\xbf>(l,+\x89YA\x97$r@\xdc\x82\xfa\xcf\xa6\xb7\xa3OnY\x9d\xdbc\x84y\xd1$\x92I\xb9<I5i\x19\x8a\x01@[;B\x0e\xa6\xe3,\xa4]`\x84\xdb\xda\xc4\x0f+\xd4\xfe\x97\x15\x83\xbf\x9dM\x8b\x8ez\xec\x98q\xf5\xb3q\xb1V\xf7\xd2\x1a$fc\xea\x16\xb9\xa9i\xde\xdc&\xcao\xd2\xb9\x83]\xbf\xfe\x16rup\xb1\xb1I\x1f\x1a\x08\x91]}\xa2\xd7\xa5\xfb\xd7-\x9f)\xd2\xd8H\xab\xf7\x8cF9\xf0\x8a\x92\xb0<l\x16!\xc1C)\xe2@\xe5{0\xaa<\xaeS8z\x144S*\xa2q@(\tm\xb7w\xc8\xda\xe3\xc9\\dN\xa6N\x91\xd6ar\xbao\xc8r\xf1\xf1\xaew\xd4\xaf\x12t\xa6\xc7I\x82>y\xe6\xc9\x91\xa6\x9eV\x9aV\xf8\x9d\x8d\xcdm$\x94#\r\xb7\x93\x11M,\x12,\xb0\xc8\xd1H\x86\xea\xealE\x1aO\x86\x13k\x04\x96\xe1\xbc\xe4\xeex\xf8\xf0\xe5*3\xe3\xb1"`,Z\xe2\xdcG/\n\xc55*6\xd1\xbb\xecv\\\x91\x15\xd0\xe6(\x05\x00\xa0\x14\x02\x80P\n\x01@\x7f\xff\xd9'


class AsyGetQQImg:
    """根据输入的参数，获取所有QQ好友的QQ号列表，下载对应QQ好友头像"""

    def __init__(self, bkn=None, cookie=None, uin_lst=None):
        """
        初始化参数
        Parameters
        ----------
        bkn: str
            请求参数
        cookie: str
            cookie
        
        Returns
        -------
            None
        """
        # 已经有qq好友qq号的情况
        if uin_lst != None:
            self.uin_lst = uin_lst
        # 有bkn, cookie的情况，需要获取qq好友qq号
        elif ((bkn != None) and (cookie != None)):
            self.bkn = bkn
            self.cookie = cookie
            self.__get_uin_lst()
        else:
            raise TypeError("please input bkn,cookie or uin_lst")

    async def __download(self, snum):
        """
        获取QQ好友头像的bytes
        Parameters
        ----------
        snum int: 
            qq号

        Returns:
        --------
        bytes:
            图片的bytes
        """
        # 获取qq头像的链接，50表示图片大小为50*50
        url = "https://qlogo4.store.qq.com/qzone/{}/{}/50".format(snum, snum)
        img = requests.get(url).content

        return img

    def __get_uin_lst(self):
        """
        获取QQ好友QQ号列表
        Parameters
        ----------
        None     

        Returns
        -------
            None
        """
        # 请求的url
        url = "http://qun.qq.com/cgi-bin/qun_mgr/get_friend_list"
        # 请求携带的参数
        payload = {"bkn": self.bkn}
        headers = {
            "cookie":
            self.cookie,
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "host":
            "qun.qq.com",
            "origin":
            "http://qun.qq.com",
            "proxy-connection":
            "keep-alive",
            "accept":
            "application/json, text/javascript, */*; q=0.01",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        # 如果参数正确应该能够获取到相应的信息
        try:
            friends_json = list(response.json()["result"].values())
        except Exception:
            raise TypeError("Please input correct params")

        # 获取每个分组，可能存在分组为空的情况
        friends_lst = []
        for friend in friends_json:
            try:
                friends_lst.append(friend["mems"])
            except Exception:
                continue

        # 提取每个好友信息中uin, 即QQ号
        self.uin_lst = [
            friend["uin"] for group in friends_lst for friend in group
        ]

    def __get_picarr(self, fpname=None, picbytes=None):
        """
        转换图片为数组
        Parameters
        ----------
        fpname str: 
            本地图片名
        picbytes bytes:
            图片的bytes

        Returns:
        --------
        图片经过numpy转换的数组:
            array
        """

        # 如果本地图片存在的话
        if fpname != None:
            # 将图片转换为数组
            img = Image.open("{}.png".format(fpname))
            mat = np.atleast_2d(img)[:50, :50, :3]
            # 过滤不满足尺寸的图片
            if mat.shape == (50, 50, 3):
                return mat

        # 如果图片的bytes存在的话
        if picbytes != None:
            img = Image.open(BytesIO(picbytes))
            mat = np.atleast_2d(img)[:50, :50, :3]
            if mat.shape == (50, 50, 3):
                return mat

        return None

    def __convert_pic(self, fpname, img):
        """
        转换图片格式
        Parameters
        ----------
        fpname str: 
            文件名
        img bytes:
            图片的bytes

        Returns:
        --------
            None
        """
        # 转换图片格式,为了获取某些格式不正确的图片，需要本机安装了`convert`
        with open("{}.jpeg".format(fpname), "wb+") as fp:
            fp.write(img)
        try:
            os.system("convert {}.jpeg {}.png".format(fpname, fpname))
        except Exception:
            pass

    async def __bytes2array(self, img):
        """
        三种方式，将bytes转换为数组
        Parameters
        ----------
        img bytes:
            图片字节流

        Returns:
        --------
        图片RGB组成的矩阵:
            array
        """

        mat = None
        num = randint(10, 1000)
        snum = str(num)

        try:
            # 字节流可以直接读取
            mat = self.__get_picarr(picbytes=img)
        except OSError:
            # 不能被直接读取，需要下载下来进行格式转换
            self.__convert_pic(snum, img)
            mat = self.__get_picarr(fpname=num)
        except Exception as e:
            # 图片不能被解析的时候，即获取失败
            print(num, e)
        finally:
            # 不论是否获取成功，将本地缓存的图片进行删除
            if os.path.exists("{}.jpeg".format(snum)):
                os.remove("{}.jpeg".format(snum))
            if os.path.exists("{}.png".format(snum)):
                os.remove("{}.png".format(snum))

        return mat

    async def __deal_img(self, loop, imgs):
        """
        将图片bytes组成的列表转换为由array组成的列表
        Parameters
        ----------
        imga list:
            图片bytes组成的列表

        Returns:
        --------
        async完成的tasks:
            list
        """
        tasks = []

        for res in imgs:
            img = res.result()

            # 当前图片不能是QQZONE默认图片
            if (img == QQZONE_ONE_BYTES) or (img == QQZONE_TWO_BYTES):
                continue

            tasks.append(loop.create_task(self.__bytes2array(img)))
        await asyncio.wait(tasks)

        return tasks

    async def __get_imgbytes(self, loop):
        """
        获取所有QQ好友头像图片bytes的列表。
        Parameters
        ----------
        
        Returns:
        --------
        async完成的tasks:
            list
        """

        tasks = [
            loop.create_task(self.__download(str(num))) for num in self.uin_lst
        ]

        await asyncio.wait(tasks)

        return tasks

    def get_array(self, save_uin_lst=False, save_pic=False):
        """
        获取所有QQ好友头像图片的矩阵。
        Parameters
        ----------
        save_uin_lst bool:
            是否保存好友列表
        save_pic bool:
            是否保存图片数组

        Returns:
        --------
        图片RGB组成的矩阵:
            array
        """
        # 保存qq好友qq号到本地
        if save_uin_lst:
            self.__save_data("uin_lst.pkl", self.uin_lst)

        loop = asyncio.get_event_loop()
        # 获取图片bytes
        tasks = loop.run_until_complete(self.__get_imgbytes(loop))
        # 根据图片bytes转换为numpy数组
        tasks2 = loop.run_until_complete(self.__deal_img(loop, tasks))
        all_pic_mat = [task.result() for task in tasks2]

        def notNone(array):
            try:
                if array.shape == (50, 50, 3):
                    return True
            except:
                pass

            return False

        pic_mat = list(filter(notNone, all_pic_mat))
        if save_pic:
            self.__save_data("pic_mat.pkl", pic_mat)

        print("总图片数:", len(all_pic_mat))
        print("失败图片数量:", len(all_pic_mat) - len(pic_mat))
        loop.close()

        return pic_mat

    def __save_data(self, fname, data):
        """
        保存数据
        Parameters
        ----------
        fpname str: 
            文件名
        data list or array:
            数据

        Returns:
        --------
            None
        """
        import pickle
        # 进行保存操作
        with open(fname, "wb+") as f:
            pickle.dump(data, f)
