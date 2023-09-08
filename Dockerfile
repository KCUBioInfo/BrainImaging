# Getting a base image from Ubuntu
FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]
LABEL maintainer="Joe Shaffer <jshaffer@kansascity.edu>"

#Update apt-get
RUN apt-get update && apt-get upgrade -y

# Install required dependencies
RUN apt-get -f install -y --fix-missing git \
    wget \
    tcsh \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    zlib1g-dev \
    libxmu-dev \
    libxi-dev \
    libxt-dev \
    libx11-dev \
    libglu1-mesa-dev \
    gcc-4.8 \
    g++ \
    gfortran \
    language-pack-en \
    gettext \
    xterm \
    x11-apps \
    csh \
    file \
    bc \
    xorg \
    xorg-dev \
    xserver-xorg-video-intel \
    libncurses5 \
    libegl1 \
    libglib2.0-0 \
    libjpeg62 \
    libwayland-client0 \
    libwayland-cursor0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-util1 \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxcb-xkb1 \
    libxft2 \
    libxkbcommon-x11-0 \
    libxkbcommon0 \
    libxrender1 \
    libxss1

RUN rm -rf /var/lib/apt/lists/*

# Set GCC version 4.8 as the default
RUN if [ -n "$(update-alternatives --list gcc)" ]; then update-alternatives --remove-all gcc; fi && if [ -e "/usr/bin/gcc-4.8" ] && [ "$(readlink -f /usr/bin/gcc)" != "/usr/bin/gcc" ]; then update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 48 --slave /usr/bin/g++ g++ /usr/bin/g++-4.8 --slave /usr/bin/gcov gcov /usr/bin/gcov-4.8 --slave /usr/bin/gfortran gfortran /usr/bin/gfortran-4.8; fi

# Download and extract Freesurfer
WORKDIR /opt
RUN wget -O freesurfer.deb https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.0/freesurfer_ubuntu22-7.4.0_amd64.deb 
RUN dpkg -i freesurfer.deb
RUN rm freesurfer.deb

# Set environment variables for Freesurfer
#ENV FREESURFER_HOME=/opt/freesurfer
ENV FREESURFER_HOME=/usr/local/freesurfer/7.4.0
ENV PATH=$PATH:$FREESURFER_HOME/bin

#Copy FreeSurfer License File to install directory
COPY license.txt $FREESURFER_HOME

# Set the working directory
WORKDIR /


