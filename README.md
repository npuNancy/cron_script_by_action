# Schedule a Python script with GitHub Actions

**Watch the video tutorial:**

[![Alt text](https://img.youtube.com/vi/PaGp7Vi5gfM/hqdefault.jpg)](https://youtu.be/PaGp7Vi5gfM)

此示例显示了如何使用GitHub Actions将Python脚本作为cron作业运行。它每周调用一次API（可以是您想要的任何计划），将响应记录在`status.log`中，并自动将更改推送到此repo。

- 在`main.py`中实现你的脚本
- 在GitHub Action `.github/workflows/actions.yml`中检查和配置cron作业
- 它可以从`requirements.txt`安装和使用第三方软件包
- 可以使用秘密环境变量。在“设置/秘密/操作”->“新建存储库秘密”中设置秘密。在`actions.yml`和`main.py`中使用相同的secret name

This example shows how to run a Python script as cron job with GitHub Actions. It calls an API once a week (could be any schedule you want), logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables can be used. Set secrets in Settings/Secrets/Actions -> 'New repository secret'. Use the same secret name inside `actions.yml` and `main.py`
