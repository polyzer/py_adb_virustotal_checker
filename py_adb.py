from adb.client import Client as AdbClient
import requests, os, sqlite3, re

class Py_Adb_Program:
    def __init__(self):
        print("program was starting")
        # Default is "127.0.0.1" and 5037
        try:
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            devices_packages = devices[0].shell("pm list packages")
            get_all_files_from_device(devices[0], devices_packages)

        except Exception as e:
            print(e)
    def print_menu(self):
        print()

    def send_all_files_to_virustotal(self, filenames):
        for fname in filenames:
            

    def make_request_and_save_answers(self, filename, scan_id, resource):
        params = {'apikey': '3f08b1ccbdf9777b5541d511bf1e3ded4f7c1347ce1e487b1fb8d3ab05761669'}
        files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        json_response = response.json()
        
        print("zatichka")

    def create_all_dbs(self):
        conn = sqlite3.connect("apkvirustotalstats.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        #Create Packages table.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pkgs 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
                name, 
                result_id
            )
        """)
        # Create virustotal responses table.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS responses
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
                permalink text, 
                resource text, 
                response_code text, 
                scan_id text,
                verbose_msg text, sha256 text
            );
                """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results
            (

            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pkg_to_result 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
                pkg_id, 
                result_id
            );
        """)

    def get_all_files_from_device(self, device, pkgs_names, pull_dir='/home/user/android_packages/'):

        pkgs_names = pkgs_names.split()

        # for i in range(len(pkgs_names)):
        #     cmd = 'adb pull '
        #     #local_pkg_path = ' /home/user/workspace/py_adb/android_pkgs/'
        #     local_pkg_path = os.getcwd()
        #     pkg_name = pkgs_names[i].split(':')[1]
        #     pkg_path = device.shell("pm path " + pkg_name).split(':')[1]
        #     filename = pkg_path.split('/').pop()
        #     pull_com =  cmd + pkg_path
        #     print(str(i) + ' ' + pull_com)
        #     os.system(pull_com)

        filelists = os.listdir('./')
        print(filelists)
        pattern = re.compile('\w*.apk$')

        # find all .apk files in current directory
        # move this file to the directory
        for fname in filelists:
            if pattern.match(fname):
                print(fname)
                os.rename('./' + fname, './android_pkgs/' + fname)
        #trying to create all needed databases;
        create_all_dbs()
        #get all files in directory
        for finame in os.listdir('./android_pkgs/'):
            #make request

if __name__ == '__main__':
