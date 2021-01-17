---
layout: post
title: VSCode lag Mac Big Sur
---

VSCode lags on Mac in the Big Sur update. Sometimes, if you hit return in an integrated terminal, and then wait 2 seconds, the whole UI will lag. It's noticeable when typing or scrolling.

The devs seem to be aware of the issue, root caused by Mac OS kernel causing certain fork operations to take a long amount of time, and hang the current process in node.

The a temporary fix until the update can be found here [https://github.com/microsoft/vscode/issues/105446](https://github.com/microsoft/vscode/issues/105446).

Running the below command and restarting VSCode will temporarily solve the issue.

```
codesign --remove-signature /Applications/Visual\ Studio\ Code.app/Contents/Frameworks/Code\ Helper\ \(Renderer\).app
```