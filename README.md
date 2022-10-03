# my-daemon
> Based on: [How to Run a Linux Program at Startup with systemd](https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/)

## A simple systemd daemon for open some apps at startup

### Follow this steps to run it:

1. copy your executable
```shell
sudo cp {your_service_executable} /usr/local/bin
```   

2. make it executable
```shell 
sudo chmod +x /usr/local/bin/{your_service_executable}
```

3. copy your service file
```shell 
sudo cp {your_service_name}.service /etc/systemd/system
```
4. change read and write permissions
```shell 
sudo chmod 640 /etc/systemd/system/{your_service_name}.service```


### Follow this to enable it:
1. check it 
```shell
systemctl status {your_service_name}.service
```

2. reload it 
```shell
sudo systemctl daemon-reload
```

3. enable it 
```shell
sudo systemctl enable {your_service_name}
```

4. start it
```shell
sudo systemctl start {your_service_name}
```

5. verify it
```shell
sudo systemctl status {your_service_name}.service
```

### Follow this to disable and remove it:
1. stop it 
```shell
sudo systemctl stop {your_service_name}.service
```

2. disable it
```shell
sudo systemctl disable {your_service_name}.service
```

3. remove your executable
```shell
sudo rm /usr/local/bin/{your_service_executable}
```

4. remove your service file
```shell
sudo rm /etc/systemd/system/{your_service_name}.service
```
