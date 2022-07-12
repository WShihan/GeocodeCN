## 关于

<img align=center src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/icon-16420027061082.png" style="zoom:30%">

<div align=center >GeocodeCN</div>



一个Qgis插件，用于地理编码，地址——> 坐标，其特点如下

> 1. 批量将地址转为坐标
> 2. 坐标转换，具备：百度坐标-->WGS84，百度坐标-->GCJ2000
> 3. 直接生成Qgis临时点图层或导出为csv文件

插件包含两个代码库，一个是github、另一个gitee

> github:https://github.com/WShihan/GeocodeCN
>
> gitee:[GeocodeCN: https://gitee.com/ShihanW/geocode-cn

***

## 使用步骤：

### 2.1 安装插件

将仓库下载或克隆到本地

> * 使用git 
>
>   ```
>   git clone https://gitee.com/ShihanW/geocode-cn
>   ```
>
> * 下载zip文件
>
>   ![image-20220110124451366](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/VWP2zMaL1FDpTxe.png)



解压后复制到QGis能识别的插件目录，步骤如下：

> 打开 Qgis --> Settings --> User Profiles --> Open Active Profile Folder
>
> ![image-20220110122357148](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/2V9AmtUTMBZEyxR.png)
>
> 之后进入 Python --> Plugins 目录下，将仓库移动到此处，接下来在Plugins，勾选它。
>
> ![image-20220112234611216](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/image-20220112234611216.png)



### 2.2 插件配置

> 2.2.1首次使用需要配置坐标系和密钥，密钥需要前往百度开放平台进行注册，这里免费提供一个试用：9IRhgisjtSA8LBnX4RwSdyHamH2jxjxm ，请求额度为：6000。![image-20220712195123022](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/image-20220712195123022.png)
>
> 配置完成，重启qgis。
>
> 

> 2.2.2选中csv文件后，指定表格中哪一列作为地址进行匹配。
>
> ![batch](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/batch.gif)
>
> 
>
> 2.2.3 匹配成功后可以生成点图层或者另存为csv文件。
>
> ![export](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/export.gif)
>
> ![saveas](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/saveas.gif)
>
> 
>
> 2.2.4 不同坐标系结果对比
>
> ![image-20220621025412703](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/image-20220621025412703.png)
>
> 
>
> 2.2.5 单各地址匹配
>
> 输入地址，点击箭头即可匹配地址，坐标系为【批量匹配】模式下选择的坐标系。
>
> ![image-20220712200127760](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/image-20220712200127760.png)



***

## 说明

> * 依赖百度地图开放接口，具体坐标精度请参考其官网。
> * 地址匹配尽量详细，如：xxx省/市/区xxx街道xxx地，若某地址未匹配成功，插件会自动省略。
> * 坐标转换依赖另一个开源库：https://github.com/wandergis/coordtransform 
> * 插件部分功能还没实现，持续更新哦，欢迎你的代码提交。
