# <p align="center">Shell scripts, data analysis and discovery, and machine learning</p>

<p align="center"><img src="../images/AdobeStock_125371270.jpeg" height="400"></p>

*Access workshop presentation slides, [click here](https://docs.google.com/presentation/d/1Y4swyDQcESyIEI9Egz3urjTbgS2qDGoaIiKeBVvFsrY/edit?usp=sharing).*

# Terminal

Your terminal will look and act differently depending on your operating system (OS). There are a variety of OSs out there including Ubuntu, Windows, Mac OS, etc. Since the majority of scientific computing is done on [Linux](https://www.linux.org/), that will be the focus of this tutorial. 

## macOS & Linux users

You are ready to proceed. Just open your terminal! I strongly suggest you pay attention to the Windows Subsystem for Linux 2 (WSL 2) set up, as you may find this useful when you develop for other OSs. 

## Windows users

The Windows Subsystem for Linux 2 (WSL2) gives you command line access to various Linux distributions. Today, we will be installing WSL2 and setting Ubuntu as our main distribution. 

To install WSL2, run the following command:

```powershell
wsl --install
```

>***Note***: If you run into errors, [click here](https://github.com/phytooracle/ASEMS_Workshop/blob/main/session2/troubleshooting.md) for troubleshooting steps.

# VSCode

We will install VSCode, an Integrated Development Environment (IDE) developed by Microsoft.

## macOS & Linux users

1. Install VSCode [here](https://code.visualstudio.com/download).

## Windows/WSL2 users

1. Install VSCode [here](https://code.visualstudio.com/download).
2. Install the Remote - WSL extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl).
   
    ![](/images/wsl_extension.png)

    ![](/images/wsl_extension_accept.png)


# Workshop prep 

1. We will download a GitHub repo containing all the files for this workshop series. To download the repo, run the following command:

    ```
    git clone git@github.com:phytooracle/AG2PI_Introduction_to_Scientific_Computing.git && cd AG2PI_Introduction_to_Scientific_Computing
    ```

2. Next we will instal Conda, which allows you to create isolated environments. These environments reduce or eliminate errors between Python libraries/packages.

    > If you are using Linux or Windows/WSL2 run:

    ```
    ./session2/prep/ubuntu_install.sh
    ```

    > If you are using MacOS run: 

    ```
    ./session2/prep/mac_install.sh
    ```



