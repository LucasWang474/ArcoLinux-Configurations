# Front-end

## pacman

```bash
sudo pacman -S babel-cli babel-core
sudo pacman -S browserify
```



## Node.js

```bash
sudo pacman -S nodejs
# sudo pacman -S nodejs-lts-gallium
```



## npm

```bash
sudo pacman -S npm

# Global
sudo su
npm i -g sass less 
npm i -g nodemon json-server

# Local
npm i express
npm i webpack@4 webpack-cli@3 --save-dev


# Update
npm update
npm update -g
```





## webpack

### Installation

> - https://webpack.js.org/guides/installation/

```bash
# Global
# npm i -g webpack@4 webpack-cli@3
npm i -g webpack webpack-cli

# Local
npm i -D webpack webpack-cli
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



## prettier

```bash
sudo pacman -S prettier
```





# Back-end

## postman

```bash
yay -S postman-bin
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

### Reset to old versions

如果你想要将软件降级为低版本的，方法类似：

```bash
# 首先克隆
git clone https://aur.archlinux.org/utools.git
cd utools

# 然后 git log 找到对应的 commit code
# 然后 git reset --hard COMMIT_CODE
git reset --hard COMMIT_CODE

# 然后 makepkg 并忽略 checksums
makepkg --skipchecksums 

# 最后安装就行了
sudo pacman -U ???.pkg.tar.zst
```

