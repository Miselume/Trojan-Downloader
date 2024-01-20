# Trojan-Downloader

**⚠️ Disclaimer: This repository is for educational and research purposes only. It is illegal to use trojan-downloader software for malicious purposes. Use this software responsibly and ethically.**

## Overview

This repository contains a sample implementation of a trojan-downloader, a type of malware that covertly downloads and executes additional malware on a victim's system. Unlike other trojan-downloaders this script not implemented another script for hiding to everyone can easily examine the script.

## Key Features

- Stealthy download a file from a specified URL
- Small payload size (less than 10 MB)
- Trojan downloader written in Python 
- Malware (file infector) written in Ruby (malware.rb)

## Trojan Downloader Explanation

**1. Remote File Download:**
- Emphasizes the ability to retrieve malicious payloads from remote sources, extending the malware's capabilities.
- Mention the use of the `requests` library for fetching the Ruby file from GitHub.

**2. File Writing:**
- Demonstrates persistence by writing the downloaded payload to the local system, ensuring its survival even after reboots.
- Detail the use of `open()` and `.write()` functions to create the "malware.rb" file.

**3. Permissions Manipulation:**
- Highlights the ability to bypass security restrictions by modifying file permissions, enabling execution.
- Describe the use of `subprocess.run(["chmod", "+x", file_path])` to grant executable permissions.

**4. Process Execution:**
- Showcases the malware's ability to launch additional malicious code, potentially leading to further infection or damage.
- Explain the use of `subprocess.run(["ruby", file_path])` to execute the downloaded Ruby script.
  
⚠️ If you want read more about malware.rb please check this [repository](https://github.com/OguzKaira/Ruby-File-Infecting-Virus-Simulation)

## Usage:

**1. Prerequisites:**
   - Ensure you have Python3 installed on your system (also Ruby).
   - Install the required libraries: `requests` and `subprocess`.
     You can do this using pip:
     ```bash
     pip install requests subprocess
     ```

**2. Running the Script:**
   - Locate the script file on your system.
   - Open a terminal or command prompt in the directory containing the script.
   - Execute the script using the Python interpreter:
     ```bash
     python <script_name>.py
     ```
      Replace `<script_name>` with the actual name of the script file.

**3. Behavior:**
   - Upon execution, the script will perform the following actions:
     - Fetch the "Malware.rb" file from the specified GitHub URL.
     - Write the downloaded file to the user's home directory as "malware.rb".
     - Grant executable permissions to the "malware.rb" file.
     - Execute the "malware.rb" file using Ruby.

**4. Caution:**
   - **Handle with extreme care.** The script is designed to simulate malware behavior and could potentially have harmful consequences.
   - **Run in a controlled environment** (e.g., a virtual machine or isolated sandbox) to prevent damage to your system or data.
   - **Understand the risks** involved before executing any unknown or potentially malicious code.


## Contributing

**Security researchers and developers are welcome to contribute to this project. Please follow these guidelines:**

- Fork the repository.
- Create a new branch for your changes.
- Make changes and commit them.
- Push your changes to your fork.
- Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact:

Oguz Kayra Buyukyildirim
oguzkairakun@gmail.com
