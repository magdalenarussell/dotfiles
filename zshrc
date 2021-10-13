clear
umask 007
# stop start output
stty -ixon
autoload -Uz compinit
compinit
export EDITOR="nvim"


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
alias quokkaclip="lemonade server -allow 128.0.0.1 & ssh -R 2489:127.0.0.1:2489 wdumm@quokka"

[ -f ~/.zshrc_machine_specific ] && source ~/.zshrc_machine_specific
