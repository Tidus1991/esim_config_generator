## About
This code allows generating flying chairs style sequences for the Multi-Object-2D simulator from [ESIM](https://github.com/uzh-rpg/rpg_esim). This code was used to generate sequences for [How to Train Your Event Camera Neural Network](https://timostoff.github.io/20ecnn), please cite this work if you use this in an academic context.
```
@Article{Stoffregen20eccv,
  author        = {T. Stoffregen, C. Scheerlinck, D. Scaramuzza, T. Drummond, N. Barnes, L. Kleeman, R. Mahoney},
  title         = {Reducing the Sim-to-Real Gap for Event Cameras},
  journal       = eccv,
  year          = 2020,
  month         = aug
}
```

## 关于esim配置生成器
esim配置生成器可以生成esim（[ESIM](https://github.com/uzh-rpg/rpg_esim)）数据仿真器的配置文件。


## 环境要求
如果想生成配置文件必须保证ros环境并安装esim，安装步骤：[here](https://github.com/uzh-rpg/rpg_esim/wiki/Installation)，如果安装成功ssim命令应该可以正常在终端内执行。

`foreground_images` 文件夹里的图像文件是最终在数据序列里前景运动的图像，其图像格式必须是4通道的png文件，在`tools`文件夹内有`jpg_to_png`小工具转换jpg到png。
`background_images` 文件夹内则是数据序列里的背景静态图像，其图像格式必须是jpg文件。
`generator_config` 文件夹里有不同参数设置的文件，例如前景图像的飞行速度等。可以按照自己的需求去调整使用。


## 如何使用
首先需要准备前景、背景图像，可以是自定义的也可以从一些数据集里抽取。
随后参考`generator_config`中的例子根据自己的需求确定参数设置文件。
运行`scripts/generate_esim2d_scenes.py`并输入参数设置文件，同时也可以在执行命令时修改参数，已经在设置文件内定义的参数会被覆盖。执行例子：
```
python scripts/generate_esim2d_scenes.py generator_config/slow_motions.json --scene_id=0 --contrast_threshold_mean=0.3 --contrast_threshold_sigma=0.1
```
这将会生成三个文件， `/tmp/000000000_autoscene.txt`, `/tmp/000000000_config2d.txt` 以及 `/tmp/esim.launch`。

随后可以使用`/scripts/2d_launch_esim.py`来生成rosbag，需要将launch文件路径作为输入，例如：
```
python scripts/2d_launch_esim.py --launch_file_path="/tmp/esim.launch"
```
最终将会得到一个rosbag数据包，其中包含了模拟事件信息与图像真值，以上的操作可以使用`2d_simulator_generator.sh`自动完成，请按需修改。


## 使用现有的配置文件生成数据集
你可以在[here](https://drive.google.com/drive/folders/1F6fNgZFmMvGkw6sAwDFE7j8Q7EH3TMve?usp=sharing)获得前景图像。
你可以在[here](https://drive.google.com/drive/folders/1ILoFnR5BHR17F0VGEzR0JIBfisw1nkc4?usp=sharing)获得相关的配置文件和场景文件。
最后运行`scripts/generate_preset.py`例如：
```python scripts/generate_preset.py /path/to/config/files```


## 更进一步的处理
`h5_generator.sh`可以帮助你批量的将rosbag转换为`.h5`文件以供导入训练模型。
`tools/loader_generator_fromh5.py`小工具可以用来生成导入训练模型所需的文件列表csv。
