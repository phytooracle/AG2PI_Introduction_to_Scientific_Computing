---
title: 'Terminal, GitHub, and iRODS Essentials'
date: 2021-09-20
permalink: /posts/2021/09/terminal-git-irods/
excerpt_separator: <!--more-->
tags:
  - terminal
  - bash
  - github
  - git 
  - irods
  - cyverse
  - data
  - science
  - computing
  - soft skills
  - linux
---

Learn how to leverage the terminal for GitHub version control and Integrated Rule-Oriented Data System (iRODS) data management!
<!--more-->
This tutorial is split into three parts: 
* **Part A**: Terminal 
   * Set up a Linux workspace for scientific computing. 
* **Part B**: GitHub
   * Build a website to share this with employers, network connections, etc. 
* **Part C**: iRODS
   * Set up iRODS within your terminal and upload/download data.  

> Tutorial requirements: 
> 
> * Computer, either Windows, Linux, or Mac OS
> 
> * CyVerse account, get one [here](https://user.cyverse.org/register)
> 
> * GitHub account, get one [here](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)

***Note: We may run into errors during this workshop. Do not be discouraged, this is part of the workspace set up. It is painful at first, but once it's over, it's worth it!***

---

# Part A: Terminal

Your terminal will look and act differently depending on your operating system (OS). There are a variety of OSs out there including Ubuntu, Windows, Mac OS, etc. Since the majority of scientific computing is done on [Linux](https://www.linux.org/), that will be the focus of this tutorial. 

## macOS & Linux users

You are ready to proceed. Just open your terminal! I strongly suggest you pay attention to the Windows Subsystem for Linux 2 (WSL 2) set up, as you may find this useful when you develop for other OSs. 

## Windows users

We need to download and install WSL 2. I use this as my go-to workspace, as it allows me to run my code on Linux but have my computer run Windows 10. You will have a Linux terminal running on the subsystem, but your main OS will be Windows! Isn't that cool?

![](/images/wsl2_example.png)

Let's get this set up on your computer by following the steps below:

1. Open Powershell as Admin and run:

    ```cmd
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```

2. Right-click on the Windows Start icon, click on Run, type ```winver```. Confirm that you meet the requirements below.

    > ***WSL 2 Requirements***
    >
    > x64 systems: Version 1903 or higher, with Build 18362 or higher.
    >
    > ARM64 systems: Version 2004 or higher, with Build 19041 or higher.

3. Enable the Virtual Machine feature by running:

    ```cmd
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

4. Download and install the Linux kernel update by [clicking here](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi).

    >***Note***: If you get an error during the Linux kernel installation, restart your computer and retry Step #5.

5. Go back to your admin Powershell window and set WSL 2 as your default WSL version by running:

    ```cmd
    wsl --set-default-version 2
    ```

6. Open the [Windows Store](https://aka.ms/wslstore) and download Ubuntu.
   
    ![](/images/ms_store_ubuntu.png)

7. Download the Windows Terminal app.
   
    ![](/images/ms_store_terminal.png)

8.  Open the Windows Terminal app. You are now ready to go! You will be asked to create a username and password. 

---

# Part B: GitHub

## Setting up SSH keys

We need to set up an SSH key to easily push changes to your repos.

1. On your terminal, run and click enter for all prompts:

    ```bash
    ssh-keygen
    ```

2. Print and copy contents of the file:

    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

3. Open [GitHub](https://github.com/), click on your Profile Picture > Settings > SSH and GPG keys > New SSH Key.
   
    ![](/images/ssh_setup.png)

4. Paste the contents of your file which you previously copied into the Key field, add a descriptive title, and click "Add SSH Key".
   
    ![](/images/add_ssh.png)

## Fork & clone a repo

1. Fork the [Academic Pages](https://github.com/academicpages/academicpages.github.io) repo.

    ![](/images/fork_repo.png)

2. Rename the repo to your GitHub username:

    ![](/images/rename_repo.png)

3. Click on the green "Code" button and copy the link to clone your own repo.

    ![](/images/clone_repo.png)

4. On your terminal, run:

    ```bash
    git clone <insert link here>
    ```

---

# Part C: iRODS Data Management

## macOS users 

1. Download the macOS installer [here](https://cyverse.atlassian.net/wiki/download/attachments/241869823/cyverse-icommands-4.1.9.pkg?version=3&modificationDate=1472820029000&cacheVersion=1&api=v2).
2. Follow the installation steps. 
3. On your terminal, run: 
   
    ```bash
    iinit
    ```

4. Fill in the prompts with:
    
    |Host name|Port #|Username|Zone|Password|
    |:--------------:|:--:|:-------------:|:----:|:--------------:|
    |data.cyverse.org|1247|CyVerse User ID|iplant|CyVerse password|

5. You're now ready to start downloading some data! 

## WSL 2 & Linux users 

1. Download the iRODS installation shell script and give it executable permissions:

    ```bash
    wget https://raw.githubusercontent.com/emmanuelgonz/emmanuelgonz.github.io/master/files/install_irods.sh 
    ```

    ```
    chmod 755 install_irods.sh
    ```

2. Run the installation script:
   
   ```bash
   sudo ./install_irods.sh
   ```

3. Log in to iRODS:
   
    ```bash
    iinit
    ```

4. Fill in the prompts with:
    
    |Host name|Port #|Username|zone|Password|
    |:--------------:|:--:|:-------------:|:----:|:--------------:|
    |data.cyverse.org|1247|CyVerse User ID|iplant|CyVerse password|

5. You're ready to start downloading some data! Let's continue our tutorial [here](https://emmanuelgonz.github.io/posts/2021/09/irods-crash-course/).

# Resources

* For details on the vim editor, run the following:

    ```bash
    vimtutor
    ```