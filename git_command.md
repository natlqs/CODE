git init        //初始化 工作区

git add 1.md        // 将1.md添加到缓冲区

git commit -m "xxxxx"       //归档

git push origin master      // 将归档的文件上传到仓库

git status              //查看当前本地仓库状态

git add.            // 将当前目录下所有文件都添加到缓冲区

git log             // 查看git提交历史

git reflog          // 查看操作记录，可以看到回滚前的哈希

git reset --mixed 53a7ca073d92a3f21e3bc53780ba15d02a5be4e9  //将缓冲区和归档区的文件进行回滚

git reset --hard        //恢复已做的更改到指定的版本，包括工作区，缓冲区，归档区

git reset --soft        //只回滚归档区

git revert 53a7ca073d92a3f21e3bc53780ba15d02a5be4e9     //将文件恢复至指定的改动之前的版本








