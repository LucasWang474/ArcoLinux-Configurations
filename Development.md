# Front-end

## npm

```bash
sudo pacman -S npm

sudo su
npm i -g sass less nodemon 


# Update
npm update
npm update -g
```



## MongoDB

```bash
yay -S mongodb-bin mongosh-bin # command line
# Or install with npm (this may fail though)
npm i -g mongosh


yay -S studio-3t # GUI
# 以特定 GTK THEME 运行 studio-3t，如 Arc-Darker
GTK_THEME=Arc-Daker studio-3t 


# 在对应开发文件夹下：
npm i mongoose
```





## Node.js

```bash
sudo pacman -S nodejs
# sudo pacman -S nodejs-lts-gallium
```





## prettier

```bash
sudo pacman -S prettier
```









# Documentation

## Zeal

> https://github.com/zealdocs/zeal

```bash
sudo pacman -S zeal
```









# ArchLinux

## Creating packages

### From old aur packages

以 uTools 为例。

**Problem:**

AUR 中 uTools 的版本为 2.4.1，但是我想提前用 beta 2.5.0 版本。

**Solution:**

```bash
# 首先克隆老版本（2.4.1）
git clone https://aur.archlinux.org/utools.git
cd utools
ls -a1

# 然后更改 PKGBUILD 和 .SRCINFO 文件中对应的变量，如 pkgver, source
# Before: pkgver=2.4.1, After: pkgver=2.5.0
# Before: source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
# After: source=("https://publish.u-tools.cn/version2/utools_2.5.0-beta.7_amd64.deb")

# 然后 makepkg 并忽略 checksums
makepkg --skipchecksums 

# ls 之后可以发现新增了 utools-2.5.0-1-x86_64.pkg.tar.zst 文件，也就是 ArchLinux 的软件包
ls -a1

# 最后安装就行了
sudo pacman -U utools-2.5.0-1-x86_64.pkg.tar.zst
```
