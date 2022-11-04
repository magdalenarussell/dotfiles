# Packages installed manually

## Youtube-dl:
manual at https://github.com/rg3/youtube-dl/blob/master/README.md#video-selection

python package, installed manually with:
```console
$ sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```

Configuration file at `~/.config/youtube-dl/config` . This includes options to be run all the time. Avoid by 	using `--ignore-config` at runtime.
***
## Wget:
Installed with Brew. To download a website recursively, not including parent directories, run 
```console
$ wget --mirror -p --html-extension --convert-links --no-parent <website url>
```
`-p`                  gets all images, etc. needed to display HTML page. 

`--mirror`            turns on recursion and time-stamping, sets infinite 
                      recursion depth and keeps FTP directory listings.

`--html-extension`    saves HTML docs with .html extensions

`--convert-links`     makes links in downloaded HTML point to local files.

`—-no-parent` 	      Ensures that no content from containing folders is downloaded.
***

## Chromaprint:
fpcalc utility downloaded from https://acoustid.org/chromaprint, copied to `/usr/local/bin`. For use in audio fingerprinting.
***

## Chrome webdriver
placed in `/usr/bin`.
***

## Autotag-mp4:
Compiled with
```console
$ pyInstaller -F autotag-mp4.py
```
and moved to `/usr/local/bin`.

***
## Manually installed LaTeX packages:
Stick'em in `/usr/local/texlive/2017basic/texmf-local/tex/latex/{package-name}/`, then run
```console
$ texhash
```
to make them visible to LaTeX. Everything in there I installed. Before, the `texmf-local` directory didn't even exist.

# Manual Settings:

## ssh
key at `~/.ssh/id_ed25519.pub` used for Gitlab and GitHub access. Private key is password protected, and password is stored in keychain by ssh according to settings in `~/.ssh/config`.

# General Notes:
## Bash settings
User settings in `~/.bash_profile` using shortcut `BashProf`

Add to path:
* by adding to to `~/.bash_profile` something like (This will only add to Bash user facing PATH when a bash session is initiated, is not global)
```console
export GOROOT=/usr/local/opt/go
export PATH=$PATH:$GOROOT/bin
```
* by adding the filepath desired to a descriptively named file in `/private/etc/paths.d/`, (this is global)
* by adding the file path desired to `/etc/paths` (requires `sudo`)

## Git
To add a remote url to a repository ???
```console
$ git remote add --
```
## Sshfs Filesystem Mount

This uses osxfuse (a cask) and sshfs packages installed with Brew.
For example, I used

```console
$ sshfs t31w454@megaplex.msu.montana.edu:/home/local/MSU/t31w454/WillGraphs /Volumes/remote -ovolname=WillGraphsRemote
```
to mount the WillGraphs directory on the remote server as the folder Volumes/WillGraphsRemote. I'm not sure what happens to the /remote subdirectory, but I was warned not to accidentally replace Volumes with my mounted directory.

## OCR scanned pdfs
Use `ocrmypdf`, possibly with the `--deskew` option if images are crooked.

If a pdf can't be read, can extract the images from it with `pdfimages` (from `poppler`, installed with Brew), then zip them back into a pdf with `img2pdf`.

```console
$ ocrmypdf input.pdf output.pdf
```

or something like:

```console
$ pdfimages input.pdf tmp/img
$ img2pdf tmp/img* -o fixed.pdf
$ ocrmypdf fixed.pdf outputwithtext.pdf
```

or the last two lines could be replaced with

```console
$ img2pdf tmp/img* | ocrmypdf - outputwithtext.pdf
```


## Compress pdf

With ghostscript:

Example usage

```console
$ gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.6 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=outfilecompressed.pdf "infile.pdf"
```

## Add Table of Contents to pdf

Use coherent pdf tools, `cpdf`.

## Convert djvu to pdf

Use djvu2pdf utility provided by homebrew


## Bash Looping

```console
$ for file in *; do python3 cpdf.py ebook "$file" "../spc/$file"; done
```

to apply the command to all files in the current folder. for another folder,

```
for file in otherfolder/*
```

for example.

## Concatenate pdfs

```console
$ pdftk 1.pdf 2.pdf cat output outfile.pdf
```
or to do all files together

```console
$ pdftk * cat output outfile.pdf
```

## Make file executable

```console
$ chmod +x file
```
(maybe there's a more specific way to do it so it doesn't grant too much permission)


## Make a pdf from a markdown file

Use the scripts that I have in my `Classes/UOTeaching/lecturenotes` directory,
they use pandoc and inject some custom latex into the header to make things
work out better.

## Remap long press caps lock and tab key on mac

Use Karabiner-Elements, with the file `capslocktab.json` in this directory. Open
the file and follow instructions in name (opening a link in a browser) to
import into Karabiner.


## Mosh/SSH through bastion server

check out tricks on https://blog.scottlowe.org/2015/11/21/using-ssh-bastion-host/

## Clipboard syncing over ssh (from remote vim, tmux, etc):

Use lemonade!

Install lemonade on both machines. The machine where you're running vim is the
client, the other is the server (so, local machine is probably server)

on local machine (server) run
```console
$ lemonade server -allow 127.0.0.1 &
$ ssh -R 2489:127.0.0.1:2489 user@host
```

Then on remote machine (client) create a `~/.config/lemonade.toml` with

```toml
port = 2489
host = 127.0.0.1
trans-loopback = true
trans-localfile = true
line-ending = 'crlf'
```

copy things for example with

```console
$ cat test.txt | lemonade copy
```

or just use nvim. As long as no preferred clipboard providers are available
(like `xclip`), it'll use lemonade automatically.

Don't forget to do `set clipboard^=unnamed` in vim if you like automatic system
clipboard integration.

In tmux, use tmux-yank according to their instructions, and set
```console
set -g @override_copy_command 'lemonade copy'
```
in `.tmux.conf`.


### Clipboard syncing over ssh or mosh or whatever using OSC 52 (preferred now):

Requires:
* mosh 1.4.0
* tmux >=3.3 (if using with mosh, otherwise version doesn't matter)
* [vim-oscyank](https://github.com/ojroques/vim-oscyank)
* a local terminal that supports OSC 52 copy e.g. iTerm 2, with the modify
    local clipboard setting turned on in preferences

Idea: the shell can modify the local clipboard via escape sequences. Tmux can
send these escape sequences on copy, as can vim via the vim-oscyank plugin.
Since they're just escape sequences, they modify your local clipboard even if
they're being sent from a machine that you're connected to via ssh, mosh, or
ssh twice, or mosh then ssh, etc.

You can test that your terminal supports OSC 52 copy by running

```console
$ printf "\033]52;c;$(printf "%s" "hello" | base64)\a"
```

after which "hello" should be in your local clipboard.

To make this work in tmux, add the following to your `tmux.conf`

```console
set -g set-clipboard on
set-option -ag terminal-overrides ",xterm-256color:Ms=\\E]52;c;%p2%s\\7"
```

If you don't intend to use mosh, the second line isn't necessary.
Now you should be able to copy to your local clipboard using copy-on-select in
tmux, even when tmux is running on a server to which you're connected via
mosh/ssh.
Again, if using mosh, you need tmux >=3.3.

To make this work in vim, install the vim-oscyank plugin, and add a convenient
mapping to copy to clipboard to your vimrc, like:

```console
nmap <leader>c <Plug>OSCYank
vnoremap <leader>c :OSCYank<CR>
```

If using tmux >=3.3, you need this in your vimrc too:

```console
let g:oscyank_term = 'default'
```

Now you should be able to copy to the local clipboard via your mapping, even
when vim is running on a remote server to which you're connected with mosh/ssh.
