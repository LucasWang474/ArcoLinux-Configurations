# 系统维护

## Ucode

```bash
sudo pacman -S amd-ucode
```

<hr>

## 设置 Grub

```bash
sudo vim /etc/default/grub
```

```bash
GRUB_TIMEOUT=1
GRUB_TIMEOUT_STYLE=hidden
```

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
reboot
```

<hr>

## 解决关机、重启时间过长

```bash
sudo vim /etc/systemd/system.conf
```

```bash
RebootWatchdogSec=10s
DefaultTimeoutStartSec=5s
DefaultTimeoutStopSec=5s
```

<hr>

## 电源管理

```bash
sudo pacman -S tlp powertop
sudo systemctl enable tlp
```

<hr>

## SSD

```bash
sudo systemctl enable --now fstrim.timer
```

<br>

<br>

# 系统设置

## Locale

```bash
sudo sed 's/#zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' -i /etc/locale.gen
sudo locale-gen
```

<hr>

## 命令行代理

我的代理配置如下：

![image-20210616231335160](Configurations.assets/image-20210616231335160.png)

在 fish 中设置命令行代理：

```bash
export http_proxy=http://127.0.0.1:1082/; export https_proxy=$http_proxy
```

可以将上面的代码设置为一个 fish abbreviation：

```bash
abbr fuck 'export http_proxy=http://127.0.0.1:1082/; export https_proxy=$http_proxy'
```

测试：

![image-20210616231721347](Configurations.assets/image-20210616231721347.png)

<hr>

## 设置默认软件

可以通过 xfce4-mime-settings 来设置默认软件，也可以通过右键点击文件来设置默认软件。

<br>

<br>

# 显示

## 解决屏幕撕裂

```bash
sudo vim /etc/X11/xorg.conf.d/20-amdgpu.conf
```

```bash
Section "Device"
	Identifier "AMD"
	Driver "amdgpu" 
	Option "TearFree" "true"
EndSection
```

<hr>

## SDDM

```bash
yay -S sddm-sugar-candy-git sddm-sugar-dark sddm-sugar-light
```

Preview:

```bash
sddm-greeter --test-mode --theme /usr/share/sddm/themes/sugar-candy
```

使用 sddm-config-editor 编辑 sddm 主题。

具体配置文件：/etc/sddm.conf

```bash
sudo vim /etc/sddm.conf
```

<hr>

## 夜间模式

```bash
sudo pacman -S redshift
```

在 i3 config 中设置自启动：

```bash
# Night mode
exec --no-startup-id redshift -P -O 5500
```

<hr>

## [Hardware video acceleration](https://wiki.archlinux.org/title/Hardware_video_acceleration)

```bash
# AMD
sudo pacman -S libva-mesa-driver mesa-vdpau
```

<hr>

## 字体

```bash
sudo pacman -S noto-fonts-cjk noto-fonts-emoji
sudo pacman -S ttf-font-awesome
```

创建 ~/.config/fontconfig/fonts.conf 文件：

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <match target="font">
        <edit mode="assign" name="hinting" >
            <bool>true</bool>
        </edit>
        <edit mode="assign" name="autohint" >
            <bool>true</bool>
        </edit>
        <edit mode="assign" name="hintstyle" >
            <const>hintslight</const>
        </edit>
        <edit mode="assign" name="rgba" >
            <const>rgb</const>
        </edit>
        <edit mode="assign" name="antialias" >
            <bool>true</bool>
        </edit>
        <edit mode="assign" name="lcdfilter">
            <const>lcddefault</const>
        </edit>
    </match>

<!-- Set preferred serif, sans serif, and monospace fonts. -->
    <alias>
        <family>serif</family>
        <prefer>
            <family>Noto Serif</family>
            <family>Noto Serif CJK SC</family>
            <family>Noto Serif CJK TC</family>
            <family>Noto Serif CJK JP</family>
            <family>Noto Serif CJK KR</family>
            <family>Droid Serif</family>
        </prefer>
    </alias>
    <alias>
        <family>sans-serif</family>
        <prefer>
            <family>Noto Sans</family>
            <family>Noto Sans CJK SC</family>
            <family>Noto Sans CJK TC</family>
            <family>Noto Sans CJK JP</family>
            <family>Noto Sans CJK KR</family>
            <family>Droid Sans</family>
        </prefer>
    </alias>
    <alias>
        <family>sans-serif</family>
        <prefer>
            <family>Noto Sans</family>
            <family>Noto Sans CJK SC</family>
            <family>Noto Sans CJK TC</family>
            <family>Noto Sans CJK JP</family>
            <family>Noto Sans CJK KR</family>
            <family>Droid Sans</family>
        </prefer>
    </alias>
    <alias>
        <family>monospace</family>
        <prefer>
            <family>Noto Sans Mono</family>
            <family>Noto Sans Mono CJK SC</family>
            <family>Noto Sans Mono CJK TC</family>
            <family>Noto Sans Mono CJK JP</family>
            <family>Noto Sans Mono CJK KR</family>
            <family>Droid Sans Mono</family>
        </prefer>
    </alias>
    <alias>
        <family>mono</family>
        <prefer>
            <family>Noto Sans Mono</family>
            <family>Noto Sans Mono CJK SC</family>
            <family>Noto Sans Mono CJK TC</family>
            <family>Noto Sans Mono CJK JP</family>
            <family>Noto Sans Mono CJK KR</family>
            <family>Droid Sans Mono</family>
        </prefer>
    </alias>

</fontconfig>
```

这样就能正常显示中文了。

<hr>

## [DPI](https://wiki.archlinux.org/title/HiDPI)

默认的 100% 缩放下标题、菜单文字还是太小了，有点伤眼睛，因此我们需要更改 [DPI](https://wiki.archlinux.org/title/HiDPI)。

通过 ~/.Xresources 文件更改 DPI：

```bash
vim ~/.Xresources
```

```bash
Xft.dpi: 110

! These might also be useful depending on your monitor and personal preference:
Xft.autohint: 0
Xft.lcdfilter:  lcddefault
Xft.hintstyle:  hintfull
Xft.hinting: 1
Xft.antialias: 1
Xft.rgba: rgb
```

DPI 默认数值为 96。如果我想要 1.15 倍缩放，那么 DPI 的数值就是 96 * 1.15 = 110。

<hr>

## 设置主题

可以通过 lxappearance 设置。

<hr>

## [Dracula](https://draculatheme.com/) color theme

### [fish](https://draculatheme.com/fish)

```bash
fisher install dracula/fish # 利用 fisher 安装
fish_config # 然后通过 fish_config 选择
```

![image-20210616233929366](Configurations.assets/image-20210616233929366.png)

<hr>

### [JetBrains](https://draculatheme.com/jetbrains)

> Go to `Plugin Marketplace`, and search `Dracula`, click `Install`.
>
> Go to `Preferences | Appearance & Behavior | Appearance`, select `Dracula` from the dropdown menu.

<hr>

### [i3wm](https://draculatheme.com/i3)

> #### Install
>
> Download using the [GitHub .zip download](https://github.com/dracula/i3/archive/master.zip) option.
>
> #### Activating the theme
>
> Append the colour palettes in `.config` to your existing i3 configuration files.

<hr>

### GTK and QT

```bash
sudo pacman -S ant-dracula-gtk-theme dracula-gtk-theme ant-dracula-kvantum-theme-git 
```

<hr>

### [Visual Studio Code](https://draculatheme.com/visual-studio-code)

> #### Install using Command Palette
>
> 1. Go to `View -> Command Palette` or press `Ctrl+Shift+P`
> 2. Then enter `Install Extension`
> 3. Write `Dracula Official`
> 4. Select it or press Enter to install

<hr>

### [Xfce4-terminal](https://draculatheme.com/xfce4-terminal)

> #### Install using Git
>
> If you are a git user, you can install the theme and keep up to date by cloning the repo:
>
> ```
> $ git clone https://github.com/dracula/xfce4-terminal.git
> ```
>
> #### Activating theme
>
> 1. Put `Dracula.theme` in `~/.local/share/xfce4/terminal/colorschemes`

