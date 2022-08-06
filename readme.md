# Meeting HUD - Head Up Display

The project's goal is to provide artificial intelligence on top of your meeting by showing every participant emotion around each people visible on screen


# Development

The project is built on a Windows machine using Powershell and Python 3. Using WSL does not work because it cannot access USB camera that the project need to access.

## Virtual environment

The project uses `conda`. 

### Install Conda

You can install conda:

```
curl https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh --output Miniconda3-py39_4.12.0-Linux-x86_64.sh 
./Miniconda3-py39_4.12.0-Linux-x86_64.sh -b
```

Add into `./zshrc` (or your terminal configuration file) the following. Ensure to change the `misterp2d` for your own username:

```
export PATH="/home/misterp2d/miniconda3/bin:$PATH"
```

Close the console, re-open and `conda` will be available.

You can now initialize your terminal: 

```
conda init zsh
```

### Activate the environment

```
conda activate meetinghud
```


### Exporting the environment

```
conda env export > environment.yml
```

### Importing the environment
```
conda env create -f environment.yml
```

# Dependencies

OpenCV Data

https://github.com/opencv/opencv/tree/master/data/haarcascades