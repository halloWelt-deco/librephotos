# Setting up a development environment

Create a directory for the project:

```sh
mkdir ~/projects/halloWelt
codedir=~/projects/halloWelt
mkdir ~/projects/halloWelt/data
mkdir ~/projects/halloWelt/data/data
mkdir ~/projects/halloWelt/data/pgAdmin
mkdir ~/projects/halloWelt/photos
cd ~/projects/halloWelt
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
cd librephotos-docker
cp halloWelt.env .env
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
codedir=/path/to/projects/halloWelt (if this doesn't work, try: ../ )
```

On Windows, copy the contents of librephotos.env to a new file called .env and get the path of the halloWelt project folder and paste it into the codedir variable.

Set the directories for the photos and data folders in the .env file:

```sh
scanDirectory=path/to/photos (if this doesn't work, try: ../photos)
data=/path/to/projects/halloWelt/data/data (if this doen't work, try: ../data/data)
pgAdminLocation=path/to/projects/halloWelt/data/pgadmin (if this doesn't work, try: ../data/pgAdmin)
```

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LibrePhotos_ownphotos&metric=alert_status)](https://sonarcloud.io/dashboard?id=LibrePhotos_ownphotos) ![Discord](https://img.shields.io/discord/784619049208250388?style=plastic) ![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&style=plastic&up_color=blue&up_message=online&url=https%3A%2F%2Flibrephotos.com)
[![Read the docs](https://img.shields.io/static/v1?label=Read&message=the%20docs&color=blue&style=plastic)](https://docs.librephotos.com/) ![GitHub contributors](https://img.shields.io/github/contributors/librephotos/librephotos?style=plastic)
<a href="https://hosted.weblate.org/engage/librephotos/">
<img src="https://hosted.weblate.org/widgets/librephotos/-/librephotos-frontend/svg-badge.svg" alt="Translation status" />
</a>

# LibrePhotos

![](https://github.com/LibrePhotos/librephotos/blob/dev/screenshots/mockups_main_fhd.png?raw=true)
<sub>Mockup designed by rawpixel.com / Freepik</sub>

- The [demo is available here](https://demo2.librephotos.com/). User is ```demo```, password is ```demo1234```.
- You can watch development videos on [Niaz Faridani-Rad's channel](https://www.youtube.com/channel/UCZJ2pk2BPKxwbuCV9LWDR0w)
- You can join our [Discord](https://discord.gg/xwRvtSDGWb).

## Installation

Step-by-step installation instructions are available in our [documentation](https://docs.librephotos.com/1/)

## How to help out
- ⭐ **Star** this repository if you like this project!
- 🚀 **Developing**: Get started in less than 30 minutes by following the [guide here](https://docs.librephotos.com/1/dev_install/)
- 🗒️ **Documentation**: Improving the documentation is as simple as submitting a pull request [here](https://github.com/LibrePhotos/librephotos.docs)
- 🧪 **Testing**: If you want to help find bugs, use the ```dev``` tag and update it regulary. If you find a bug, open an issue.
- 🧑‍🤝‍🧑 **Outreach**: Talk about this project with other people and help them to get started too!
- 🌐 **Translations**: Make LibrePhotos accessible to more people with [weblate](https://hosted.weblate.org/engage/librephotos/).
- 💸 [**Donate**](https://github.com/sponsors/derneuere) to the developers of LibrePhotos

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

## What does it use?

- **Image Conversion:** [ImageMagick](https://github.com/ImageMagick/ImageMagick) 
- **Video Conversion:** [FFmpeg](https://github.com/FFmpeg/FFmpeg)
- **Exif Support:** [ExifTool](https://github.com/exiftool/exiftool)
- **Face detection:** [face_recognition](https://github.com/ageitgey/face_recognition) 
- **Face classification/clusterization:** [scikit-learn](https://scikit-learn.org/) and [hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
- **Image captioning:** [im2txt](https://github.com/HughKu/Im2txt), 
- **Scene classification** [places365](http://places.csail.mit.edu/)
- **Reverse geocoding:** [Mapbox](https://www.mapbox.com/): You need to have an API key. First 50,000 geocode lookups are free every month.
