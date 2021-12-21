# Do not run this script as root.
if os.geteuid() == 0:
    print("Please run this script as non-root user.")
    sys.exit(1)


# Install ArcoLinux packages from `packages.txt` using `yay`.
print("\n\n\nInstalling ArcoLinux packages...")
with open("packages.txt", "r") as f:
    for line in f:
        subprocess.run(["yay", "-S --needed --noconfirm", line.strip()])

    print("Installed ArcoLinux packages from `packages.txt`.")


# Change default shell for user lucas to `fish`
subprocess.run(["chsh", "-s", "/usr/bin/fish", "lucas"])
print("Changed default shell for user `lucas` to `fish`.")


# Download dotfiles from `https://github.com/LucasWang474/Dotfiles`
repo = "https://github.com/LucasWang474/Dotfiles"
# # First set system proxy
# os.system("export http_proxy=http://127.0.0.1:1081/; export https_proxy=$http_proxy;")
# print("Set system http proxy to `http_proxy=http://127.0.0.1:1081/`.")

# Then clone the repo
subprocess.run(["git", "clone", repo])

# Copy all files in `Dotfiles` to `$HOME`
print("Copying files in `Dotfiles` to `$HOME`...")
shutil.copytree("Dotfiles", os.environ["HOME"])
print("Copied all files in `Dotfiles` to `$HOME`.")


# All done!
print("\n\n\nAll done!")
print("Please reboot the system.")
print("Enjoy!")
print("Lucas Wang")
