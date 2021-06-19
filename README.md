# 安装 ArcoLinux-i3wm 之后的配置

## 搭建基础环境

### 安装 fish

生活苦短，我用 fish。

`Mod+Enter` 打开终端。（Mod 指 Windows 键）

```bash
sudo pacman -Syy fish
chsh -s /bin/fish # 更换当前用户默认的 shell 为 fish
```

然后按 `Mod+x`，选择 `Logout`，重新登录。

<hr>

### 使用 Xfce4-terminal

目前 Arcolinux 默认使用的是 terminal 终端，但它使用起来依然不是很无脑，因此我推荐使用已经预装好的 Xfce4-terminal。

首先打开 i3 config 文件。

```bash
vim .config/i3/config
```

然后找到下行：

```bash
bindsym $mod+Return exec --no-startup-id termite;focus
```

将其中 termite 更换为 xfce4-terminal

```bash
bindsym $mod+Return exec --no-startup-id xfce4-terminal;focus
```

后面的几行可以全部注释。

```bash
# bindsym $mod+KP_Enter exec --no-startup-id termite;focus
# bindsym control+mod1+t exec --no-startup-id termite; focus
# bindsym control+mod1+Return exec --no-startup-id termite; focus
# bindsym control+mod1+KP_Enter exec --no-startup-id termite; focus
```

然后 `Mod+Shift+R` 重启 i3。此时按下 `Mod+Enter` 即可启动 Xfce4-terminal，右键选择 Preferences 即可设置。

小提示：你也可以按 F12 启动 drop-down xfce4-terminal。

<hr>

### 设置 Rofi

rofi 是一个软件启动器。

打开 i3 config，找到下面一行：

```bash
bindsym $mod+F12 exec --no-startup-id rofi -show run -font "Noto Sans 13"
```

将其更改为：

```bash
bindsym $mod+d exec --no-startup-id rofi -show run -font "Noto Sans 13"
```

然后重启 i3。试试 `Mod+d` 启动 rofi。

小提示：你可以使用 rofi-theme-selector 来选择 rofi 主题。

<hr>

### 设置亮度

有些机器亮度不是开箱即用的，下面使用 brightnessctl 来调节亮度。

```bash
sudo pacman -Syy brightnessctl
brightnessctl set 30%
```

在 i3 config 中设置：首先找到此行

```bash
bindsym XF86MonBrightnessUp exec --no-startup-id xbacklight -inc 20 # increase screen brightness
bindsym XF86MonBrightnessDown exec --no-startup-id xbacklight -dec 20 # decrease screen brightness
```

然后将这两行注释，并在其后加上

```bash
bindsym XF86MonBrightnessUp exec --no-startup-id brightnessctl -q s +5%
bindsym XF86MonBrightnessDown exec --no-startup-id brightnessctl -q s 5%-
```

然后重启 i3。试试笔记本的亮度调节按键。

<hr>

### 更新系统

现在可以正式开始舒舒服服地配置系统了！

自动生成中国源：

```bash
sudo reflector -c China --save /etc/pacman.d/mirrorlist --sort rate
```

看看都自动生成了哪些：

```bash
cat /etc/pacman.d/mirrorlist
```

添加 ArchLinuxCN 源：

```bash
sudo vim /etc/pacman.conf
```

```bash
# 在 /etc/pacman.conf 尾部添加下面几行
# 可以参考、对比上面的 ArchLinux 源，然后你就知道怎么自己添加 ArchLinuxCN 源了（cat /etc/pacman.d/mirrorlist）

[archlinuxcn]
Server = http://mirror.lzu.edu.cn/archlinuxcn/$arch
# Server = http://mirrors.bfsu.edu.cn/archlinuxcn/$arch
```

```bash
sudo pacman -Syy
sudo pacman -S archlinuxcn-keyring
```

最后更新系统：

```bash
sudo pacman -Syyu
reboot
```

如果在关机界面卡死了，直接断电就行了。关于这方面的配置可以看我的 [Configurations.md](Configurations.md)。

<hr>

### 安装搜狗输入法

```bash
yay -S fcitx-im fcitx-configtool fcitx-sogoupinyin fcitx-qt5 fcitx-qt4
```

在 i3 config 中设置 fcitx 自启动：

```bash
# Input method
exec --no-startup-id fcitx
```

设置输入法的环境变量：

```bash
# 如果你使用的是 startx，那就 vim ~/.xinitrc
# 不想用 ~/.xprofile，用 ~/.pam_environment 也可以

vim ~/.xprofile
```

```bash
# 加入以下三行

export XMODIFIERS=@im=fcitx
export QT_IM_MODULE=fcitx
export GTK_IM_MODULE=fcitx
```

然后打开 fcitx-configtool，在 Input Method 中添加 sogoupinyin。

![image-20210616221727216](README.assets/image-20210616221727216.png)

然后重启或者重新登录，之后按 Shift 键打开输入法（假设你已经按照我说的设定了自启动）。

<hr>

### 安装 VSCode

```bash
sudo pacman -S visual-studio-code-bin
```

然后安装 i3 语法高亮插件。之后就可以使用 VSCode 愉快地配置了。

![image-20210616224342729](README.assets/image-20210616224342729.png)

<hr>

### 安装浏览器

```bash
sudo pacman -S google-chrome
```

<hr>
### 文件浏览器

已经预装好了 Thunar 文件浏览器，使用 Win+Shift+Enter 打开。

<hr>

### 安装网络代理软件

#### v2ray + qv2ray

```bash
sudo pacman -S v2ray qv2ray
```

在 i3 config 中设置 qv2ray 自启动：

```bash
# Proxy
exec --no-startup-id qv2ray
```

qv2ray 在重新登录之后会出 bug，无法正常启动，可以创建下面的脚本：

```bash
touch ~/.config/qv2ray/init.sh
chmod u+x ~/.config/qv2ray/init.sh
vim ~/.config/qv2ray/init.sh
```

```bash
#!/bin/bash

killall v2ray
killall qv2ray
sleep 2
exec qv2ray
```

然后将上面的脚本放入 i3 config 中，并注释之前的自启动代码：

```bash
# Proxy
# exec --no-startup-id qv2ray
exec --no-startup-id ~/.config/qv2ray/init.sh
```

<hr>

#### SwitchyOmega

Google Chrome 无法直接设置代理，而是依赖于系统的代理。我们可以使用 SwitchyOmega 完成浏览器的代理配置。

下载链接：https://github.com/FelisCatus/SwitchyOmega/releases/download/v2.5.20/SwitchyOmega_Chromium.crx

然后将下载好的文件的 crx 后缀改为 zip，再在 Google Chrome 中打开 chrome://extensions/，开启 Developer mode，将 zip 文件拖入即可完成安装。

<br>


SwitchyOmega 的配置：

GFW list: https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt

![image-20210616225010112](README.assets/image-20210616225010112.png)

![image-20210616225020862](README.assets/image-20210616225020862.png)

注意：SOCKS 的端口号取决于你的代理软件的具体配置。例如，我的 Qv2ray 是这样配置的：

![image-20210616225251440](README.assets/image-20210616225251440.png)

<hr>

**到此为止，基本的环境搭建已经完成了，后面的配置都是个人喜好问题了。**

**本文后面的是软件推荐，更多的系统层次的配置可以看 [Configurations.md](Configurations.md)**。

除此之外，还可以参考我的 https://github.com/LucasWang474/Dotfiles。**<u>*（可以试试新装一个系统，然后直接把它复制且替换到 $HOME/ 下，然后看看效果）*</u>**

小提示：你可以使用 xfce4-appfinder 查看已安装的软件。快捷键是 Alt+F3。

<hr>

<br>

<br>

## 日常软件

### 下载软件

#### 百度网盘

```bash
yay -S baidunetdisk-bin
sudo ln -s /usr/lib/baidunetdisk/baidunetdisk /usr/bin/baidunetdisk

mkdir ~/Downloads/BaidunetdiskDownloads # 然后在百度网盘中设置默认下载位置
```

小提示：可以使用 Ctrl+-/= 来放大缩小。

#### 迅雷

```bash
yay -S xunlei-bin
mkdir ~/Downloads/XunleiDownloads # 然后在迅雷中设置默认下载位置
```

<hr>

### 解压缩

对于在中文环境下使用 zip 压缩的文件，在 Linux 下解压可能会出现乱码的情况。下面介绍解决方案，更多请参考[官方文档](https://wiki.archlinux.org/title/Localization_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)/Simplified_Chinese_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#zip_%E5%8E%8B%E7%BC%A9%E5%8C%85%E4%B9%B1%E7%A0%81)。

```bash
yay -S unzip-iconv

# 然后使用下面这条指令来解压
unzip -O gbk ARCHIVE_NAME.zip

# 可以将它设置为 fish abbr
abbr unzipgbk 'unzip -O gbk'
```

<hr>

### 播放器

```bash
# mpv 其实非常好用，可能是 linux 下最好用的播放器了
sudo pacman -S mpv

sudo pacman -S netease-cloud-music
```

**小技巧：netease-cloud-music 设置缩放**

```bash
sudo vim /usr/bin/netease-cloud-music
```

```bash
export QT_SCALE_FACTOR=1.4
```

<hr>

### PDF

#### 阅读器

```bash
sudo pacman -S okular
```

#### 编辑器

```bash
yay -S masterpdfeditor-free
```

<hr>

### Markdown

```bash
sudo pacman -S typora
```

<hr>

### 思维导图

```bash
yay -S xmind-2020
```

<hr>

### 图像编辑器

```bash
sudo pacman -S gimp
```

<hr>

### 录屏

```bash
sudo pacman -S simplescreenrecorder
sudo pacman -S screenkey # print keys on the screen as you are entering
```

<hr>

### 截图

```bash
sudo pacman -S flameshot
```

在 i3 config 中添加下列代码：

```bash
bindsym $mod+c mode "$screenshot"

set $screenshot (alt+a)rea, (alt+s)ingle screen, a(alt+l) screens, save (Shift+s)ingle screen, save a(Shift+l)l screens, (alt+c)onfig
mode "$screenshot" {
    # Some tools (such as import or xdotool) might be unable to run 
    # upon a KeyPress event, because the keyboard/pointer is still grabbed. 
    # For these situations, the --release flag can be used, which will 
    # execute the command after the keys have been released.

    bindsym mod1+a --release exec flameshot gui
    
    bindsym mod1+s --release exec flameshot screen -c
    bindsym Shift+s --release exec flameshot screen -p ~/Pictures/
    
    bindsym mod1+l --release exec flameshot full -c
    bindsym Shift+l --release exec flameshot full -p ~/Pictures/
    
    bindsym Shift+l --release exec flameshot full -p ~/Pictures/

    bindsym mod1+c --release exec flameshot config
    
    bindsym Return mode "default"
    bindsym Escape mode "default"
}
```

然后通过 Win+c 启动 flameshot binding mode。

<hr>

### 闹钟

```bash
sudo pacman -S gnome-clocks
```

<hr>
<br>

<br>

## 学习软件

### Anki

```bash
sudo pacman -S anki
```

<hr>

### Goldendict

```bash
sudo pacman -S goldendict hunspell hunspell-en_US
```

下载词典：https://freemdict.com/category/%e8%8b%b1%e8%af%ad/

<br>

<br>

## 编程软件

### fish

```bash
# 去除 greeting
set -U fish_greeting ""

# 插件管理器
yay -S fisher

# 配置 fish
fish_config
```

一些插件

> - [awesome.fish](https://github.com/jorgebucaran/awesome.fish)

- [fish-abbreviation-tips](https://github.com/Gazorby/fish-abbreviation-tips)

  ```bash
  fisher install Gazorby/fish-abbreviation-tips
  ```

- [z](https://github.com/jethrokuan/z) 

  **z** is a port of [z](https://github.com/rupa/z) for the [fish shell](https://fishshell.com/).

  ```bash
  fisher install jethrokuan/z
  ```

<hr>

### Git

```bash
git config --global user.email "474.lucas.wang@gmail.com"
git config --global user.name "Lucas Wang"
git config --global credential.helper store # 保存账号密码
```

<hr>

### Java

```bash
sudo pacman -S jdk8-openjdk openjdk8-doc
sudo pacman -S jdk11-openjdk openjdk11-doc

sudo pacman -S intellij-idea-ultimate-edition intellij-idea-ultimate-edition-jre
sudo ln -s ~/.config/fish/fish_variables /opt/intellij-idea-ultimate-edition/plugins/terminal/fish/fish_variables
```

#### Intellij Plugins

- Dracula Theme
- Atom Material Icons
- Material Theme UI

#### Set default Java environment

```bash
sudo archlinux-java status
sudo archlinux-java set java-X-openjdk
```

<hr>

### Python

```bash
sudo pacman -S python python-pip
sudo pacman -S ipython jupyter-notebook
sudo pacman -S pycharm-community-edition
```

