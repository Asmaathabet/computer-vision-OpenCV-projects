# Computer Vision Projects using OpenCV :

## Virtual environment to run the packages: <br/>

To run the virtual environment for packages <br/>
1- open powershell <br/>
2- navigate to the project routes <br/>
3- type: `cv_env\Scripts\activate` <br/>
if the script didn't work : <br/>

- open powershell as adminstrator <br/>
- type : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` <br/>
- type Y for yes <br/>
- close powershell & repeat the steps again. <br/>

4- it should show something like this : <br/>
![alt text](image.png) <br/>
5- install `pip install opencv-python mediapipe==0.10.9 pyautogui protobuf==3.20.3`
<br/>

6- type `python -c "import mediapipe as mp; print(mp.__version__)"` to check if its installed correctly <br/>
it should shows: 0.10.9

7- force VS CODE to use the venv <br/>

- Open VS Code <br/>
- Press Ctrl + Shift + P <br/>
- Select Python: Select Interpreter <br/>
- Choose THIS EXACT PATH: <br/>
  {your_project_route}\cv_env\Scripts\python.exe <br/>
- Restart VS Code completely <br/>
