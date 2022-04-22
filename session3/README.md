# Signing up for GitHub and creating your first repo

### Go to github.com and click 'sign up' in the top right hand corner and follow the prompts.
![Screenshot from 2022-04-21 19-49-21](https://user-images.githubusercontent.com/64273464/164575672-6e1c2949-4870-45c4-855d-db8129ae7ab7.png)

### Click create repository on the left hand side.
![Screenshot from 2022-04-21 19-52-52](https://user-images.githubusercontent.com/64273464/164575805-2a199e50-c39b-4a6d-bdcd-a94d91a44cbf.png)

### Name the repository and click add README.md
![Screenshot from 2022-04-21 20-08-09](https://user-images.githubusercontent.com/64273464/164575904-3870f246-6c04-46ec-a541-e1817d9019ee.png)

### Congradulations!
![Screenshot from 2022-04-21 20-08-19](https://user-images.githubusercontent.com/64273464/164575993-b8c9f22c-e0d6-4cd9-8f3b-6c06351c9647.png)

# Making a change from the command line

## Creating an oauth key

### Click the icon in the top right hand side and go to settings
![Screenshot from 2022-04-21 20-00-51](https://user-images.githubusercontent.com/64273464/164576159-d0b84b20-071d-4f90-a40b-b29cd760b65c.png)

### Scroll all the way down and click developer settings on the left hand side
![Screenshot from 2022-04-21 20-01-06](https://user-images.githubusercontent.com/64273464/164576278-27477b55-c2c8-4a60-b333-aff6fb04f3ac.png)

### Click personal access tokens on the left
![Screenshot from 2022-04-21 20-01-33](https://user-images.githubusercontent.com/64273464/164576310-8f49f867-a566-452d-a2b2-03b8c67a282e.png)

### Click generate new token on the right
![Screenshot from 2022-04-21 20-01-33](https://user-images.githubusercontent.com/64273464/164576355-1ec768eb-204e-43b4-ae74-102bc00d450c.png)

### Give it a nickname, and just check the box shown
![Screenshot from 2022-04-21 20-02-24](https://user-images.githubusercontent.com/64273464/164576373-282244ba-33b8-4b89-8134-073f5f001da1.png)

### *COPY THE STRING OF LETTERS IN THE GREEN BOX AND SAVE THEM FOREVER*

## Making a change to your repo

### Navigate to your repo click the green code dropdown box, and copy the link
![Screenshot from 2022-04-21 20-10-36](https://user-images.githubusercontent.com/64273464/164576581-f396d90c-8927-452e-a419-9d9bd15a7b12.png)

### Open your terminal and follow the instructions below to clone the repo, make a change, and have those changes saved in the remote repository

`cd`
`git clone {paste the link here}`
`cd {repo name}`

Use vscode or your IDE of choice in order to create a python script called test.py in this folder.

`git add test.py`
`git commit -m 'testing'`
`git push`

Enter your github user name
Enter your oauth code you saved
press enter

Refresh your repo on your browser to see the changes reflected.


## Contributing to a colaborators code

Naviate to https://github.com/phytooracle/AG2PI_Introduction_to_Scientific_Computing

### Click fork in the top right hand
![Screenshot from 2022-04-21 20-30-03](https://user-images.githubusercontent.com/64273464/164577243-0d34d1c0-26a5-4a14-8537-a45dd859f6f1.png)

### Click create fork
![Screenshot from 2022-04-21 20-30-15](https://user-images.githubusercontent.com/64273464/164577286-0276b804-ca70-4f03-9048-02c6c835c3be.png)

### You are now on your own fork of our repo
![Screenshot from 2022-04-21 20-30-32](https://user-images.githubusercontent.com/64273464/164577365-ca6360b2-ca43-498a-8399-711cc858ea49.png)

### Clone the repo using the terminal just as we did before
### Navigate to session3/response_scripts
### Create a script using vscode or another IDE with a print statement that gives feedback on the workshop
### add, commit, and push the changes to the new script, just as above

### Return to your github repo and click contribute
![Screenshot from 2022-04-21 20-32-52](https://user-images.githubusercontent.com/64273464/164577600-6ef2d750-40c5-4ef0-ad66-be9f66b400b9.png)

### Click open pull request
![Screenshot from 2022-04-21 20-33-03](https://user-images.githubusercontent.com/64273464/164577633-3f1e6639-cb2f-4f51-8688-a5393deb7bc3.png)

### Click create pull request
![Screenshot from 2022-04-21 20-33-16](https://user-images.githubusercontent.com/64273464/164577711-cae1b9a5-2d62-4729-a811-e62dd67ed54f.png)

### Name the pull request and click create pull request
![Screenshot from 2022-04-21 20-33-39](https://user-images.githubusercontent.com/64273464/164577733-de78cfe7-082b-4c35-be7b-4d85d246dc36.png)

## Congrats! You have contributed to your repository as well as a collaborators, you are well on your way to mastering version control!



