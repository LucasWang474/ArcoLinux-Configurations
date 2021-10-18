# Front-end

## grab color

Create a shell script:

```bash
#!/usr/bin/env bash

xcolor | tr -d '\n' | xsel -b
```

Modify permission:

```bash
chmod u+x FILE_PATH
```

Hard link it to `/bin`:

```bash
sudo ln FILE_PATH /bin/grabc
```

Now try to run it with rofi.





# Shell

## [tldr](https://tldr.sh/)

```bash
sudo pacman -S tldr
```

