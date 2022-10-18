# JourneyLink
<p align="center">
  <img src="https://github.com/halloWelt-deco/librephotos/blob/dev/screenshots/logo-white.png?raw=true" />
</p>
<sub>Track your memories</sub>

![](https://github.com/halloWelt-deco/librephotos/blob/dev/screenshots/jl-dash.png?raw=true)

![](https://github.com/halloWelt-deco/librephotos/blob/dev/screenshots/journeylink.png?raw=true)

- The hosted application is available here at [https://hallowelt.r18i.me](https://hallowelt.r18i.me/). Username is ```user```, password is ```hallowelt```.
- The Kickstarter video for the project is available [here]().
- You can watch a demo of the interface [here](https://drive.google.com/file/d/12ieg5h2e1IVvF9cSXfctiMNAWiMT3QmY/view?usp=sharing).

---
## Usage Guide

A typical user workflow is as follow:

### On Desktop:

1.) The user visits https://hallowelt.r18i.me, they sign up and create an account. For purposes of the demo, the username is ```user``` and password is ```hallowelt```.

2.) If they want to start location tracking, they click on the "Configure Location Tracking on your phone" button. As they are on desktop, a QR code to the config URL is displayed and they scan it with their phone.
3.) Once they have scanned the QR Code on their phone, the owntracks app is downloaded and configured automatically.

4.) They can upload photos through the desktop, and view their location tracks in the map.

### On Phone:

1.) The user visits https://hallowelt.r18i.me, (optionally they can use the Add to Home Screen button in Chrome to add the PWA to their phone), they sign up and create an account.

2.) If they want to start location tracking, they click on the "Configure Location Tracking on your phone" button. As they are on phone, clicking on the button will automatically redirect them to the configuration URL(https://hallowelt.app.link/user) and OwnTracks is downloaded and configured automatically.

This link has to be accessed from the user’s mobile device for the user’s configuration to be pulled in automatically.  When downloading OwnTracks for the first time from this screen, please head back to the User Trips page and once again click on the Config button once the app has finished downloading in order to pull in the user configuration.

3.) The user returns back to the JourneyLink web app in browser (or the PWA).

4.) They can upload photos through their phone, and view their location tracks in the map.

A demo of this process is shown here: [JourneyLink Location Tracking Setup](https://drive.google.com/file/d/1lPj0mJ1qofD7UmBRM7p3a17qmehmz6G5/view?usp=sharing).

### Setting up automatic photo syncing from phone:
1.) To setup automatic photo syncing, the user needs to download the NextCloud mobile application - [Android](https://play.google.com/store/apps/details?id=com.nextcloud.client) / [iOS](https://apps.apple.com/au/app/nextcloud/id1125420102).

The configuration URL for the NextCloud app is https://nchw.r18i.me/

The username and password are the same ones as the JourneyLink account - Username: ```user``` Password: ```hallowelt```

2.) Once configured, the user can go to the Settings and choose which folders they’d want to automatically sync from their phone onto JourneyLink. 

A demo of this process is shown here: [JourneyLink Photo Syncing Setup](https://drive.google.com/file/d/1lITccxy385yTOoXH5hG8iUXRrOjvF3SA/view?usp=sharing).

---
# Setting up a development environment

Create a directory for the project:

```sh
mkdir ~/projects/hallowelt
codedir=~/projects/hallowelt
mkdir ~/projects/hallowelt/data
mkdir ~/projects/hallowelt/data/data
mkdir ~/projects/hallowelt/data/pgadmin
mkdir ~/projects/hallowelt/photos
cd ~/projects/hallowelt
```

On Windows, create a folder called halloWelt and navigate to it in PowerShell. Create halloWelt/data/data, halloWelt/data/pgAdmin and photos folders.

Pull frontend codebase:

```git
git clone https://github.com/halloWelt-deco/librephotos-frontend.git
```

Pull backend codebase:

```git
git clone https://github.com/halloWelt-deco/librephotos.git
```

Pull docker repo:

```git
git clone https://github.com/halloWelt-deco/librephotos-docker.git
```

Set environment variables:

```sh
cd ~/projects/hallowelt/librephotos-docker
cp hallowelt.env .env
```

Run the docker containers:

```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

If you want access to the logs of the running containers use the following command instead:

```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

If you use Visual Studio Code, you can also benefit from auto-completion and other goodies. For this, just run 

```sh
code .
```

in your Dockerfile folder, which is ~/projects/halloWelt/librephotos-docker.

Visual Studio Code will open and ask you if you want to reopen it in the container. If you do, it will create the images from scratch (first time you do it can take a couple of minutes), and you will have the same Python interpreter LibrePhotos uses internally - and hence the same installed libraries in auto completion, and the same development environment, will be shared by all devs. This includes tools like isort, flake8 and pylint.

Alternatively, you can run the Remote-Containers: Open Folder in Container command from the Command Palette. Note in order to open this container, you must have the required dependencies installed. More details can be found here.

Read the docs at:

https://docs.librephotos.com/5/dev_backend/

https://docs.librephotos.com/5/dev_frontend/


## If you are using a different directory structure from what was outlined at the beginning, read this next part:

Edit the codedir variable in the .env file:

```sh
codedir=/path/to/projects/halloWelt #(if this doesn't work, try: ../ )
```

On Windows, copy the contents of librephotos.env to a new file called .env and get the path of the halloWelt project folder and paste it into the codedir variable.

Set the directories for the photos and data folders in the .env file:

```sh
scanDirectory=path/to/photos #(if this doesn't work, try: ../photos)
data=/path/to/projects/halloWelt/data/data #(if this doen't work, try: ../data/data)
pgAdminLocation=path/to/projects/halloWelt/data/pgadmin #(if this doesn't work, try: ../data/pgAdmin)
```
---
## Features

  - Support for all types of photos including raw photos
  - Support for videos
  - Timeline view
  - Scans pictures on the file system
  - Multiuser support
  - Generate albums based on events like "Thursday in Berlin"
  - Face recognition / Face classification
  - Reverse geocoding
  - Object / Scene detection
  - Semantic image search
  - Search by metadata

---
## What does it use?

- **Image Conversion:** [ImageMagick](https://github.com/ImageMagick/ImageMagick) 
- **Video Conversion:** [FFmpeg](https://github.com/FFmpeg/FFmpeg)
- **Exif Support:** [ExifTool](https://github.com/exiftool/exiftool)
- **Face detection:** [face_recognition](https://github.com/ageitgey/face_recognition) 
- **Face classification/clusterization:** [scikit-learn](https://scikit-learn.org/) and [hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
- **Image captioning:** [im2txt](https://github.com/HughKu/Im2txt), 
- **Scene classification** [places365](http://places.csail.mit.edu/)
- **Reverse geocoding:** [Mapbox](https://www.mapbox.com/): You need to have an API key. First 50,000 geocode lookups are free every month.

## Technical Architecture
![](https://github.com/halloWelt-deco/librephotos/blob/dev/screenshots/JourneyLink_Tech_Architecture.jpg?raw=true)
