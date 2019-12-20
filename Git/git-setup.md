# Git
Setup git on your mac


## Generating SSH key
SSH to generate as per machine.

`ssh-keygen -t rsa -b 4096 -C “test@gmail.com”`

`pbcopy < ~/.ssh/id_rsa.pub`

pbcopy will copy SSH key to your clipboard.
Now paste this SSH key in **Github** or **BitBucket** in Account Settings.

## Create Repository

Create repo from Github or Bitbucket account.
You will receive SSH Key like
>git@github.com:your-account/repo-name.git

Copy this and paste in our terminal
`git clone git@github.com:your-account/repo-name.git`

a folder will be created check this with :
`ls -l`