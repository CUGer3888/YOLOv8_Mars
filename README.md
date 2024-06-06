火星图片来源：https://moon.bao.ac.cn/Mars/index/index.html#

配合使用截图代码快速截图

感谢武大学长 戴维难 的帮助，教程：https://www.bilibili.com/video/BV1nx4y187Po/

可能遇到的问题如下：

1.anaconda的安装
  教程：https://www.bilibili.com/video/BV1Fy4y1878z/
  
2.cuda、cudnn的安装
  教程：https://www.bilibili.com/video/BV1fY411y7Xq/
  
  首先查看pytorch支持的最高版本
  
  PyTorch网址:https://pytorch.org/

  然后查看N卡系统支持最高的版本
  
  然后权衡下载支持最高版本的CUDA和cuDNN

  CUDA工具包： https://developer.nvidia.cn/zh-cn/cuda-toolkit

  cuDNN：https://developer.nvidia.com/rdp/cudnn-download

  配置对应的环境变量

  nvcc -V：查看版本CUDA

  安装项目依赖

  pip install -e ultralytics

  pip install ultralytics

  pip install yolo

3.正确，快速安装CPU版本pytorch和torchvision
  教程：https://blog.csdn.net/shiwanghualuo/article/details/122860521

  打开pytorch官网
  
  找到对应CUDA版本的下载链接

  在pyharm中使用pip安装，得到下载地址，终止程序，前往download.pytorch.org/whl/torch_stable.html下载对应当前电脑的版本

  同理torchvision也一样，注意对应版本一致
  
4.labelstudio的使用

  教程：https://www.bilibili.com/video/BV1Ht4y1d7Yr/
