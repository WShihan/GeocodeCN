## 关于

<img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/pic/icon-16420027061082.png" alt="icon" style="zoom: 25%;" />

<div align=center >GeocodeCN</div>



一个Qgis插件，用于地理编码，地址——> 坐标，其特点如下

> 1. 批量将地址转为坐标
> 2. 坐标转换，具备：百度坐标-->WGS84，百度坐标-->GCJ2000
> 3. 直接生成Qgis临时点图层或导出为csv文件

***

## 使用：

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



### 2.2 使用插件

> 2.2.1选中csv文件后，指定表格中哪一列作为地址进行匹配。
>
> ![操作](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/%E6%93%8D%E4%BD%9C.gif)
>
> 
>
> 2.2.2 匹配成功后可以生成点图层或者另存为csv文件。
>
> ![保存和添加图层](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/%E4%BF%9D%E5%AD%98%E5%92%8C%E6%B7%BB%E5%8A%A0%E5%9B%BE%E5%B1%82.gif)
>
> 
>
> 2.2.3 不同坐标系结果对比
>
> ![image-20220621025412703](https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/image-20220621025412703.png)
>
> 2.2.4 单各地址匹配
>
> 输入地址，点击箭头即可匹配地址，坐标系为【批量匹配】模式下选择的坐标系。
>
> <img src="https://md-1301600412.cos.ap-nanjing.myqcloud.com/gitUse/image-20220621030318805.png" alt="image-20220621030318805" style="zoom:50%;" />



***

## 说明

> * 依赖百度地图开放接口，具体坐标精度请参考其官网。
> * 地址匹配尽量详细，如：xxx省/市/区xxx街道xxx地，若某地址未匹配成功，插件会自动省略。
> * 坐标转换依赖另一个开源库：https://github.com/wandergis/coordtransform 
> * 插件部分功能还没实现，持续更新哦，欢迎你的代码提交。
