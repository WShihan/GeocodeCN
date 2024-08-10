## GeocodeCN

![GitHub Repo stars](https://img.shields.io/github/stars/WShihan/GeocodeCN?style=plastic) ![GitHub repo size](https://img.shields.io/github/repo-size/WShihan/GeocodeCN?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/WShihan/GeocodeCN?style=plastic) ![GitHub](https://img.shields.io/github/license/WShihan/GeocodeCN?style=plastic)

## 1. 介绍

<p align="center">
<img src="./icon.png" alt="fd" style="width:60px;margin: 0px auto" /></p>


GeocodeCN是一个Qgis插件，用于地理编码，地址——> 坐标，其特点如下

> 1. 批量将地址转为坐标
> 2. 坐标转换，具备：百度坐标-->WGS84，百度坐标-->GCJ2000
> 3. 直接生成Qgis临时点图层
> 4. 将结果导出为csv文件



## 2. 使用步骤：

### 2.1 安装插件

2.1.1 下载zip格式仓库文件压缩包。

![image-20220110124451366](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/VWP2zMaL1FDpTxe.png)



2.1.2 在QGSI里打开插件管理页面，选择`Insall from ZIP`，选择上一步下载的zip文件

![image-20240811023822744](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811023822744.png)

点击`installed`查看是否安装成功

![image-20240811024354440](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811024354440.png)



### 2.2 插件配置

 首次使用需要配置坐标系和密钥，密钥需要前往百度开放平台进行注册，这里免费提供一个试用：`9IRhgisjtSA8LBnX4RwSdyHamH2jxjxm` ，请求额度为每日6000。

 ![image-20240811024516533](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811024516533.png)

 配置完成，可能需要重启qgis。



### 2.3 使用

1.批量匹配

选中csv文件后，指定表格中哪一列作为地址进行匹配。

可在配置区，设置坐标系。

![image-20240811025611843](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811025611843.png)



2.单次匹配

![image-20240811030328494](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-20240811030328494.png)



可将匹配结果导入地图查看或导出为包含坐标值的csv文件。



不同坐标系结果对比

![](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/typora/image-2022062102541270_clip.png)











***

## 3. 说明

> * 依赖百度地图开放接口，具体坐标精度请参考其官网。
> * 地址匹配尽量详细，如：xxx省/市/区xxx街道xxx地，若某地址未匹配成功，插件会自动省略。
> * 坐标转换依赖另一个开源库：https://github.com/wandergis/coordtransform 
> * 插件部分功能还没实现，持续更新哦，欢迎你的代码提交。
