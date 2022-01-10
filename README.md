## GeocodeCN

一个Qgis插件，用于地理编码，地址——> 坐标，其特点如下

> 1. 批量将地址转为坐标
> 2. 坐标转换，具备：百度坐标-->WGS84，百度坐标-->GCJ2000
> 3. 直接生成Qgis临时点图层或导出为csv文件

## 使用方法：

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
> 之后进入 Python --> Plugins 目录下，将仓库移动到此处。

### 2.2 使用插件

> 2.2.1选中csv文件后，指定文件中那一列作为地址进行匹配
>
> ![start](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/KocL9Pvth1pMquX.gif)
>
> 2.2.2 匹配成功后可以生成点图层或者另存为csv文件
>
> ![export](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/Kme14OroIJQGqav.gif)
>
> 2.2.3 指定输出坐标，这里需要修改源码，进入插件（仓库）目录下，找到gcs.py文件，修改transform参数：
>
> * None :表示原始坐标系，即百度坐标系
> * bd2wgs：表示转为WGS84坐标系
> * bd2gcj：表示转为国测局坐标系
>
> ![image-20220110124548760](https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/eAThH18ot6ZuUfQ.png)



## 说明

> * 依赖百度地图开放接口，具体坐标精度请参考其官网。
> * 建议匹配地址尽量详细，如：xxx省/市/区xxx街道xxx地。
> * 坐标转换依赖另一个库：https://github.com/wandergis/coordtransform 
