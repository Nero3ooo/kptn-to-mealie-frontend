# Kptn to Mealie Frontend

This is a lightweigth web frontend to add recipes from KptnCook to Mealie via the shared link. <br/>
The app is designed as pwa and so it can be installed as web-app on mobile devices via chrome. 

Many thanks to https://github.com/ephes/kptncook for the backend functionality. <br/>
Also a big thank you for your fantastic cooking apps @[Mealie](https://mealie.io/) and @[KptnCook](https://www.kptncook.com/). 

## Disclaimer
This app is work in progress and should not be exposed. <br/>
I only wanted to have a quick solution to add recipes from KptnCook to Mealie.

## Installation
Please install the backend first: https://github.com/ephes/kptncook 

After that you need to install flask:
```
pip install flask
```
Now you can clone the repository and start the frontend.

## Start Application
To start the flask app just execute it:
```
python3 app.py
```
Afterwards you can reach the app at port 5000.

<img width="289" alt="image" src="https://github.com/user-attachments/assets/8a0c70aa-7b64-437f-8631-1f86884fcf0e" />

If you install it as PWA on your smartphone, you can use the share handler functionality to transfer a recipe within three clicks:

Click on share recipe in the KptnCook-App and select KptnToMealie. 

The link of the recipe should be passed to the inputfield automaticly and you can transfer it to mealie by clicking the button.
