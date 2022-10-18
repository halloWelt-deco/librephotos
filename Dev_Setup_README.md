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


#### If you are using a different directory structure from what was outlined at the beginning, read this next part:

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
