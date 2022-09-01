# This ubuntu image allows us to access the container using vnc 
# for debugging
FROM dorowu/ubuntu-desktop-lxde-vnc

# First install required dependencies
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4EB27DB2A3B88B8B
RUN apt-get update -y
RUN apt-get install wget xz-utils xvfb python3 pip git ncat -y

# Install tor
RUN wget -q -c https://dist.torproject.org/torbrowser/11.5.1/tor-browser-linux64-11.5.1_en-US.tar.xz && \
    tar -xf tor-browser-linux64-11.5.1_en-US.tar.xz && \
    rm -f tor-browser-linux64-11.5.1_en-US.tar.xz

# Install gecko driver and put the binary in bin
RUN wget -q -c https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz && \
    tar -xf geckodriver-v0.31.0-linux64.tar.gz && \
    mv geckodriver /bin && \
    rm geckodriver-v0.31.0-linux64.tar.gz

# Copy all local files to the python directory, because most of them need to be there
COPY . ./python

# Install python dependencies
RUN pip install -r ./python/requirements.txt

# Move a custom prefrences file into the tor browser configuration folder.
# This prefrences file has quickstart enabled
RUN mv ./python/prefs.js ./tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default/prefs.js

# move the main run script to root
RUN mv ./python/run.sh .

# === Code for demonstratoin ===
# move the urls test file ino root
RUN mv ./python/urls.txt .