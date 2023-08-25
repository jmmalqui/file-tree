# File-Tree

Makes a File Tree out of a directory.

Output:

```txt
└──file-tree   1   1 / 1
   ├──.git 10   1 / 5
   │  ├──COMMIT_EDITMSG 101   1 / 12
   │  ├──config 101   2 / 12
   │  ├──description 101   3 / 12
   │  ├──FETCH_HEAD 101   4 / 12
   │  ├──HEAD 101   5 / 12
   │  ├──hooks 101   6 / 12
   │  │  ├──applypatch-msg.sample 1011   1 / 14
   │  │  ├──commit-msg.sample 1011   2 / 14
   │  │  ├──fsmonitor-watchman.sample 1011   3 / 14
   │  │  ├──post-update.sample 1011   4 / 14
   │  │  ├──pre-applypatch.sample 1011   5 / 14
   │  │  ├──pre-commit.sample 1011   6 / 14
   │  │  ├──pre-merge-commit.sample 1011   7 / 14
   │  │  ├──pre-push.sample 1011   8 / 14
   │  │  ├──pre-rebase.sample 1011   9 / 14
   │  │  ├──pre-receive.sample 1011   10 / 14
   │  │  ├──prepare-commit-msg.sample 1011   11 / 14
   │  │  ├──push-to-checkout.sample 1011   12 / 14
   │  │  ├──sendemail-validate.sample 1011   13 / 14
   │  │  └──update.sample 1011   14 / 14
   │  ├──index 101   7 / 12
   │  ├──info 101   8 / 12
   │  │  └──exclude 1011   1 / 1
   │  ├──logs 101   9 / 12
   │  │  ├──HEAD 1011   1 / 2
   │  │  └──refs 1011   2 / 2
   │  │     ├──heads 10110   1 / 2
   │  │     │  └──main 101101   1 / 1
   │  │     └──remotes 10110   2 / 2
   │  │        └──origin 101100   1 / 1
   │  │           └──main 1011000   1 / 1
   │  ├──objects 101   10 / 12
   │  │  ├──0d 1011   1 / 9
   │  │  │  └──c7b4b001b8af6250cc8a88aec74562fcd1bb27 10111   1 / 1
   │  │  ├──21 1011   2 / 9
   │  │  │  └──a83e2dd6fa24b7e5a2eefb70bf8b2fd547825a 10111   1 / 1
   │  │  ├──5a 1011   3 / 9
   │  │  │  └──53d9d5a1c106665f17523d6ec992438a59066a 10111   1 / 1
   │  │  ├──c7 1011   4 / 9
   │  │  │  └──97acc8df9f8ed4528a504e3f2ee5de61209ab9 10111   1 / 1
   │  │  ├──d3 1011   5 / 9
   │  │  │  └──8aa2967d6fae9f7f0da13a8633e04634796993 10111   1 / 1
   │  │  ├──f6 1011   6 / 9
   │  │  │  └──e59c3360f625ad21b4a6c0e1468201a39115f2 10111   1 / 1
   │  │  ├──fe 1011   7 / 9
   │  │  │  └──fae64ddb91987dce8f9b03780568902f711c44 10111   1 / 1
   │  │  ├──info 1011   8 / 9
   │  │  └──pack 1011   9 / 9
   │  ├──ORIG_HEAD 101   11 / 12
   │  └──refs 101   12 / 12
   │     ├──heads 1010   1 / 3
   │     │  └──main 10101   1 / 1
   │     ├──remotes 1010   2 / 3
   │     │  └──origin 10101   1 / 1
   │     │     └──main 101010   1 / 1
   │     └──tags 1010   3 / 3
   ├──.gitignore 10   2 / 5
   ├──.vscode 10   3 / 5
   │  └──settings.json 101   1 / 1
   ├──file-tree.py 10   4 / 5
   └──README.md 10   5 / 5
```
