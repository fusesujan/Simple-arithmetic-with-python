
## GIT
<p>Python functions for basic mathematical operations such as addition, subtraction, and multiplication. These functions should take two numeric inputs and return the result of the corresponding operation.
Initialize the git. Add proper commit message and push codes to the git repository
Create a feature branch with Gitflow. Add a function in the previous script to calculate the division and merge using Gitflow
Create a release branch with Gitflow.
.</p>

## Steps followed: 
### Initial setup
 - Create an account with fusemachine personal gmail.
 - Generate and Add SSH key to github with current github. ( In case of dual account make config file in local .ssh directory and add  both of the key there and in github as well. Have to be carefull while pulling and cloning from gitub.)
- Generate the personal access token for this account as well, it may required in future, while pushing.
 - Create an repository on github.
### Code
- Write the code to perform only those operations which you want to be there except division.
- Initiliaze git and (add, commit, add remote and push it on **default** Main/Master branch).
>I perfer managing flow by manually with CLI rather than, with the package gitflow.
- Make new branch feature from the present default branch and checkout to that branch.

	`git branch -b feature`

	`git checkout feature`
- (optional pull that default branch iff requried ), `git pull origin Master` . Now make changes on code, add functionality to perform division as well.
- Now add, commit, and push it on **feature** branch, After that checkout to that default branch and Merge it with feature branch .
- In case you want to merge it by creating **Pull request** , Go to pull request page of that repository in github and follow the procedure OR else you may done it from VS code as well.
- Regarding **release** branch, Create this branch from that default branch where all the updated code is present. And further work can be done with creating new branch Or even with that feature branch, And merging them on release branch if you want to go for production with this branch / make it a major branch.
----

## Local Hooks:

<p>Implement a pre-commit hook script to detect whether the email set in the repository is correct or not. Also, implement a script to detect if there are any trailing whitespaces in the commit.
 Implement a pre-commit hook with the pre-built plugins. 
Use this plugin to manage the pre-commit hook. Implement a commit-msg hook to check if the commit message contains tags for commit types such as “feat”, “fix”, “refactor” etc.</p>

#### First write the script for implimenting initial problem only. 

- To make .git folder visible in vscode, go to setting and search **exclude**, scroll and you will get .git , click the cross icon located in rightmost side of that text. 
- go to that directory and make pre-commit named file. And write script to detect if there are any trailing whitespaces in the commit or not.  Make  it executable with `chmod +x pathtothatfile `. And try commiting with whitespace it should give warning/error but depends on script code.

#### Now it is mentioned to do all this with pre-commit , package of python. . 
-  Please visit this in order to understand better about [pre-commit](https://pre-commit.com/) .
- Follow the steps :
	`pip install pre-commit`
	create a file named `.pre-commit-config.yaml`. And put :
	```
	repos:
		- repo: https://github.com/pre-commit/pre-commit-hooks
          rev: v2.3.0
          hooks:
              -id: check-yaml
              -id: trailing-whitespace 
  ```
	Now generate the hook script with
	`pre-commit install`
- Here only existing hooks check-yaml and trailing-whitespace is used , we have many existing hooks like this from pre-commit-hooks library. You can visit this . [Available hooks](https://pre-commit.com/hooks.html)
- Here we have to check valid user.email in github config , trailing whitespaces and commit message conventions , for this , I made two files commit-msg-check.sh  and  email-validation-and-commit-convention.sh inside  the hooks folder and used both of them in yaml file . 
``` 
	repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.0.1
        hooks:
          - id: trailing-whitespace
          - id: check-yaml

      - repo: local
        hooks:
          - id: email-validation-and-commit-convention
            name: Validate Email ,Commit -msg convention
            entry: .git/hooks/email-validation-and-commit-convention.sh
            language: script
            types: [file]

      - repo: local
        hooks:
          - id: commit-msg-check
            name: Check Trailing Whitespaces in Commit Message
            entry: .git/hooks/commit-msg-check.sh
            language: script
            types: [file] 	
```
- And run this again `pre-commit install`. after which then This works for commit message trailing whitespace, commit message convention and also for the email set in the repository is correct or not.
