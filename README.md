# File Management System Application for Encryption
## How to run
- Download the folder: [here](https://drive.google.com/drive/folders/1Acya-9g4gRrcfIn2cdsAxTy1S_igSvA2?usp=sharing)
- Double click on `FileManagementSystem.exe`
## How it builds 🔨
- Python
- PyQt6
  - QTDesigner
  - PyUIC

## System Design
When the user first enters the system, they are required to choose a path for saving the files that will be generated by the application. Then, the user is required to sign up for an account. Once the user signs up for an account, the user’s username and the hash value of the password combined with the username (hash(password || username)) will be stored in the users.json file which is placed in the “config” folder. By combining the password with the username to create the hash value, it can be ensured that each user has a unique hash.

**Folder Structure of the Application**
![image](https://github.com/user-attachments/assets/51a9beba-1953-4e44-9f10-cb76d4af7314)

Moreover, when a user creates an account. A folder named after the username will be generated in the user folder of the system, to save the data about that user. Inside the user’s folder, it will create a config folder to save the user’s public key file. For each user, the program will generate two folders(“passEncrypt” and “keyEncrypt”) to save the encrypted files. For “keyEncrypt” folder, it contains the “keys” folder which will save all the generated encrypted symmetric key files, and the “files” folder which will save all the files that are encrypted by the public key encryption. For “passEncrypt” folder, it contains files that are encrypted by the passphrase.
