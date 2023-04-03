# 浮动挡板
> 用于阻挡字幕的简单应用，永远置顶

<p>
  <a href="https://raw.githubusercontent.com/songquanpeng/block-board/main/LICENSE">
    <img src="https://img.shields.io/github/license/songquanpeng/block-board?color=brightgreen" alt="license">
  </a>
  <a href="https://github.com/songquanpeng/block-board/releases/latest">
    <img src="https://img.shields.io/github/v/release/songquanpeng/block-board?color=brightgreen&include_prereleases" alt="release">
  </a>
  <a href="https://github.com/songquanpeng/block-board/releases/latest">
    <img src="https://img.shields.io/github/downloads/songquanpeng/block-board/total?color=brightgreen&include_prereleases" alt="release">
  </a>
</p>

可在 [Release 页面](https://github.com/songquanpeng/block-board/releases)下载最新版本（Windows，macOS，Linux）。

## 功能
- 永远置顶；
- 使用鼠标滑轮设置透明度；
- ESC 键退出；

## 打包流程
```bash
pip install -r requirements.txt
pyrcc5 -o resource_rc.py resource.qrc 
pyinstaller --noconsole -F ./main.py --icon icon.ico -n board.exe
```
