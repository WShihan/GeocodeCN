## GeocodeCN

![GitHub Repo stars](https://img.shields.io/github/stars/WShihan/GeocodeCN?style=plastic) ![GitHub repo size](https://img.shields.io/github/repo-size/WShihan/GeocodeCN?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/WShihan/GeocodeCN?style=plastic) ![GitHub](https://img.shields.io/github/license/WShihan/GeocodeCN?style=plastic)

## 1. 介绍

<p align="center">
<img src="./icon.png" alt="fd" style="width:60px;margin: 0px auto" /></p>


GeocodeCN是一个QGIS插件，用于地理编码，地址——> 坐标，其特点如下

> - 支持批量/单个将地址转为坐标
>
> - 支持不同地图平台，百度地图，OSM，Here，Mapbox
>
> - 百度地图支持转换：百度坐标 --> WGS84，百度坐标 --> GCJ2000
>
> - 支持直接生成QGIS临时点图层
>
> - 支持将结果导出为csv文件



## 2. 使用步骤：

### 2.1 安装插件

2.1.1 下载zip格式仓库文件压缩包。

![image-20220110124451366](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/VWP2zMaL1FDpTxe.png)



2.1.2 在QGSI里打开插件管理页面，选择`Insall from ZIP`，选择上一步下载的zip文件

![image-20240811023822744](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811023822744.png)

点击`installed`查看是否安装成功

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811024354440.png" alt="image-20240811024354440" style="width:100%;" />



### 2.2 插件配置

 首次使用需要配置密钥然后选择使用哪一个`服务`（有些地图服务需要配置坐标系，比如百度地图），密钥需要前往地图服务平台获取。

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241106234932211.png" alt="image-20241106234932211" style="width:70%;" />

 配置完成，可能需要重启qgis。



### 2.3 使用

1.批量匹配

选中csv文件后，指定表格中哪一列作为地址进行匹配。

可在配置区，设置坐标系。

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241106235141869.png" alt="image-20241106235141869" style="width:70%;" />



2.单次匹配

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20241106235635927.png" alt="image-20241106235635927" style="width:70%;" />



可将匹配结果导入地图查看或导出为包含坐标值的csv文件。



不同坐标系结果对比

![](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-2022062102541270_clip.png)











***

## 3. 说明

> * 依赖地图平台开放接口，具体坐标精度请参考其官网。
> * 地址匹配尽量详细，如：xxx省/市/区xxx街道xxx地，若某地址未匹配成功，插件会自动省略。
> * 百度地图坐标转换依赖另一个开源库：https://github.com/wandergis/coordtransform 
> * 插件部分功能还没实现，持续更新哦，欢迎你的代码提交。
