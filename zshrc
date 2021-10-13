## antigen stuff
source $HOME/.antigen/antigen.zsh
# Load the oh-my-zsh's library.
antigen use oh-my-zsh
#antigen bundle virtualenv
#antigen bundle virtualenvwrapper
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-history-substring-search
antigen theme https://gist.github.com/willdumm/c672692545433a858303c079b64955ca gallifrey-nve
# Tell antigen that you're done.
antigen apply

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

alias fhsnail="mosh wdumm@snail.fhcrc.org"
[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh
