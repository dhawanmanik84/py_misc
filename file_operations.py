


def update_server_config(file_path, key, value):
#read the configuration file
    with open(file_path, "r") as file:
        lines = file.readlines()

#update the config value for the specified key
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                #update new value
                file.write(key + "=" + value + "\n")
            else:
                #no change
                file.write(line)

server_config_file = 'server.conf-fileoperations'
key_to_update = 'MAX_CONNECTIONS'
new_value = '600' #new value

update_server_config(server_config_file, key_to_update, new_value)

#update_server_config("server.conf", "MAX_CONNECTIONS", "1000")