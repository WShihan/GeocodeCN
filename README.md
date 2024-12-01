![GitHub Repo stars](https://img.shields.io/github/stars/WShihan/GeocodeCN?style=plastic) ![GitHub repo size](https://img.shields.io/github/repo-size/WShihan/GeocodeCN?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/WShihan/GeocodeCN?style=plastic) ![GitHub](https://img.shields.io/github/license/WShihan/GeocodeCN?style=plastic)

## 1. 介绍

<p align="center">
<img src="./icon.png" alt="fd" style="width:60px;margin: 0px auto" /></p>



这是一个[QGIS](https://www.qgis.org)插件，主要用于批量地理编码，即将地址转为坐标。它本身附带用户操作界面（GUI），开箱即用，即便你不会编程，也能轻松上手。

其特点如下：

> - 支持批量/单个将地址转为坐标
>
> - 支持对接国内外不同地图平台，百度地图，高德地图，OSM，Here，Mapbox
>
> - 支持坐标转换：百度坐标 --> WGS84，百度坐标 --> GCJ2000
>
> - 支持直接生成QGIS图层预览
>
> - 支持将结果导出为csv文件
>
> - 支持部分地图服务设置代理



## 2. 使用步骤：

使用插件的一个前提是必须先安装[QGIS](https://www.qgis.org/)，这是一个开源GIS软件，可运行在`Windows`，`MacOS`，`Linux`等操作系统之上，功能强大，而且它是免费使用的，任何人都能获取它的代码然后修改和分发。



### 2.1 安装

该插件已发布在QGIS官方插件库，可直接在仓库里查找安装，或者通过下载源码包安装。

2.1.0 通过QGIS插件仓库安装

前往菜单 `Plugin` >> `Manage and Install Plugins`。

搜索`geocodecn`安装。

![image-20241129233401416](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241129233401416.png)



2.1.1 通过下载zip压缩包安装。

前往[代码仓库](https://github.com/WShihan/GeocodeCN)页面下载zip压缩包

![image-20241201141510531](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241201141510531.png)



2.1.2 在QGSI里打开插件管理页面，点击`Insall from ZIP`，选择上一步下载的zip文件

![image-20240811023822744](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811023822744.png)

点击`installed`查看是否安装成功

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241109001045554.png" alt="image-20240811024354440" style="width:100%;" />



### 2.2 配置

 ==首次使用需要配置密钥==，然后选择使用哪一个`地图服务`（有些地图服务需要配置坐标系，比如百度地图），密钥需要前往对应地图服务平台注册获取。

<p align="center">
<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241201142155238.png" alt="image-20241106234932211" style="width:70%;" />
</p>


==⚠注意==：OSM地图服务由于在中国被屏蔽，无法正常访问，需要做一些特殊的网络配置，如果你有其他的代理地址，可以填写并使用它。



### 2.3 坐标匹配

1.批量匹配

需要将所有地址保存到一个CSV，然后在插件里选中它，接着指定表格中哪一列作为`地址`进行匹配。



```
id,address, name, prop1
1, xx省xx市xxx区xx街道xx, xx大学, 985
1, xx省xx市xxx区xx街道xx, xx大学,211
1, xx省xx市xxx区xx街道xx, xx大学,无
1, xx省xx市xxx区xx街道xx, xx大学，无
```

<center>这是一份参考的CSV字段格式，字段多少不限制，只要保证里面有一个地址字段就行</center>



==⚠注意==：插件会自动检测CSV的编码，如果检测结果不对，需要用户手动选择编码。

<p align="center">
<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241106235141869.png" alt="image-20241106235141869" style="width:70%;" />
</p>


2.单次匹配

在地址栏内输入地址，即可进行匹配。

<p align="center">
<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241106235635927.png" alt="image-20241106235635927" style="width:70%;" />
</p>


### 2.4 生成图层

点击`添加到地图`，将会生成一个QGIS图层，同时会将CSV里的其他字段写入图层属性表里。

![](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-2022062102541270_clip.png)

<center>不同坐标系结果对比</center>



### 2.5 导出为CSV

点击`导出为`将匹配结果导出为CSV文件，插件将在原来的文件基础之上，添加匹配结果，即新增两个字段，一个经度，另一个纬度。





***

## 3. 说明

> * 地址匹配结果的精度依赖地图平台开放接口，具体精度请参考其官网。
> * 请合规使用插件，在使用地图平台服务的同时务必遵守平台规范。
> * 匹配的地址尽量详细，如：xxx省/市/区xxx街道xxx地，若某地址未匹配成功，插件会自动省略。
> * 百度地图坐标转换依赖另一个[开源库](https://github.com/wandergis/coordtransform)
> * 插件部分功能还没实现，持续更新哦，欢迎你的代码提交。
