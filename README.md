# Dotfiles Installation

To install, run

```console
git clone git@gitlab.com:willdumm/dotfiles.git ~/.dotfiles --recursive
cd ~/.dotfiles
./install
```

It may be necessary to run `:PlugInstall` on first run of (n)vim to resolve
errors.

Dotfile links are managed by Dotbot.

## Zsh
Machine-specific config (such as autojump location) is located in
`~/.zshrc_machine_specific`. This is not tracked by dotbot

Antigen may need to be installed.

## Other useful utilities:
* [nvim](https://neovim.io)
* [autojump](https://github.com/wting/autojump)
* [ag](https://github.com/ggreer/the_silver_searcher)
* [fd](https://github.com/sharkdp/fd)


