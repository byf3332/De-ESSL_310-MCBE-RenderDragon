# De-ESSL_310-MCBE-RenderDragon
## Introduction

Remove ESSL_310 shader of Minecraft Bedrock Edition from **CRAPPY RenderDragon**

Please use Python 3.10.x to run (Written under Python 3.10.11)

No external requirements needed (Only the built-in json module)

## 介绍

从Minecraft基岩版的**垃圾渲染龙**里移除可能导致卡顿的ESSL_310相关文件

请使用Python 3.10.x运行（使用Python3.10.11编写）

无额外依赖（仅调用内置json模块）

------------------------------------------------------------------------------------
## Usage

1. Clone this repository.
2. Go to the repository directory.
3. Put your unpacked renderer material in a folder, which should look like ``/xxx/yyy/zzz/RendererSrc/``. Under``RenderSrc`` there should be the separate folders for renderers, like ``Actor``, ``ActorBanner``, ``ActorBannerForwardPBR``.
4. Execute ``python main.py``
5. The program asks for ``Workdir: ``, enter the the path ``/xxx/yyy/zzz/RendererSrc/`` you created before.
6. Press enter and wait for the program to run.
7. After running the files in your path ``/xxx/yyy/zzz/RendererSrc/`` will be modified, where ``ESSL_310`` files will be deleted, and the json file also auto-processed.

## 使用方法

1. 克隆本仓库。
2. 进入仓库目录。
3. 将已解包的renderer material放在一个文件夹中，这个文件夹应该看起来像 ``/xxx/yyy/zzz/RendererSrc/``。在``RenderSrc``文件夹下应该有各个渲染器的单独目录，比如 ``Actor``、``ActorBanner``、``ActorBannerForwardPBR``。
4. 执行 ``python main.py``
5. 程序显示 ``Workdir: ``，输入之前创建的路径 ``/xxx/yyy/zzz/RendererSrc/``。
6. 回车，等待程序运行。
7. 运行结束后，``/xxx/yyy/zzz/RendererSrc/`` 中的文件将被修改，其中 ``ESSL_310`` 相关的文件将被删除，json 文件也将被自动处理。





