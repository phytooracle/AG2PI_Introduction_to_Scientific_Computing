If you run into errors with the single command install, these steps should help!

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