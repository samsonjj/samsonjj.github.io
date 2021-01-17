---
layout: post
title: Bash Lazy Loading NVM
---

I was practicing rust in vim when I noticed it always took a second or two to compile and run my programs while inside of vim. This lead to a couple of learnings.

1) Vim creates a new zsh terminal each time you execute an external command.

For example, running `!cargo build` inside of Vim, causes vim to essentially run the equivalent of `$SHELL -c "{cmd}"`. This means that my .zshenv file was getting sourced every time. The solution... use my zsh configuration files as they were meant to be used. [Here is the zsh docs on that.](http://zsh.sourceforge.net/FAQ/zshfaq03.html#l19) .zshenv is sourced on each new zsh session, but .zprofile and .zlogin are only sourced when logging in. So I moved most of my configuration to .zprofile, where it should really be. This sped up the time it took to run vim commands to the point where it is pretty much instant.

2) Initializing nvm is slow

Admittedly, this makes sense. But it was running every time I ran a Vim command, causing the commands to be slow. Moving the nvm initialization stuff to .zprofile fixed my current issue, but now I feel like making my logins fatser as well. We can lazy load nvm by creating a function which wraps nvm, and only loads nvm on the first call.

```
# .zprofile

# Lazy loading nvm
export NVM_LOADED=false
nvm() {
    if [ "$NVM_LOADED" = false ]; then
        load_nvm
        NVM_LOADED=true
    fi
    nvm $@
}
```


nice.