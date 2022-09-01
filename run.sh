# This is the main run script that should be used by the end user

# run tor browser through a virtual frame buffer
xvfb-run ./tor-browser_en-US/Browser/firefox > /dev/null &

# check the tor network every 5 seconds until it has connected
while : ; do
    sleep 5
    python ./python/testTorNetwork.py > /dev/null  
    return_code=$?
    if [ $return_code == 0 ]
    then
        break
    fi
    printf "\n\n\t\tNOT CONNECTED YET\n\n"
done

# once connected run scraper.py with the provided arguments
printf "\n\n\t\tTor proxy: ready\n\n"
python ./python/scraper.py $1 $2
kill 0

