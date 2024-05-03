import os
import sys
import psutil

# Get the path to the user's home directory
home_dir = os.path.expanduser("~")
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
frontend_dir = os.path.join(root_dir, 'Frontend')

# Get the path to the system's PATH directory
path_dir = os.path.join(home_dir, "AppData", "Local", "Microsoft", "WindowsApps")

# Create the batch file with the alias if it doesn't exist
batch_file_path = os.path.join(path_dir, "ControlApp.bat")
if not os.path.exists(batch_file_path):
    with open(batch_file_path, "w") as f:
        f.write(f"@echo off\n")
        f.write(f"python {os.path.join(root_dir, 'CLI', 'ControlApp.py')} %*\n")

    # Add the batch file to the system's PATH
    if path_dir not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + path_dir


def check_frontend_running():
    try:
        output = os.popen('tasklist /FI "IMAGENAME eq node.exe" /NH').read()
        return "node.exe" in output
    except Exception as e:
        print("----------------------------------------------------------------")
        print(f"Error checking frontend process: {e}")
        print("----------------------------------------------------------------")
        return False


def check_backend_running():
    try:
        output = os.popen('tasklist /FI "IMAGENAME eq uvicorn.exe" /NH').read()
        return "uvicorn.exe" in output
    except Exception as e:
        print("----------------------------------------------------------------")
        print(f"Error checking backend process: {e}")
        print("----------------------------------------------------------------")
        return False


def print_process_info(pid):
    try:
        process = psutil.Process(pid)
        print("-----------------------------------------------------------------------------\n")
        print(f"Process ID: {pid}")
        print(f"Process Name: {process.name()}")
        print(f"Process Executable: {process.exe()}")
        print(f"Process Working Directory: {process.cwd()}")
        print(f"Process Status: {process.status()}")
        print(f"Process Memory Usage: {process.memory_info().rss / (1024 ** 2):.2f} MB")
        print("----------------------------------------------------------------------------\n")
    except psutil.NoSuchProcess:
        print("----------------------------------------------------------------\n")
        print("Process information not available.")
    except Exception as e:
        print("----------------------------------------------------------------\n")
        print(f"Error retrieving process information: {e}")


def start_frontend():
    if check_frontend_running():
        print("Frontend is already running")
        return
    print("----------------------------------------------------------------\n")
    print("Starting frontend...")
    os.chdir(frontend_dir)
    os.system('START /B npm run start:frontend')
    print("Frontend started successfully.")
    print_process_info(os.getpid())
    print("----------------------------------------------------------------\n")


def start_backend():
    if check_backend_running():
        print("Backend is already running")
        return
    print("----------------------------------------------------------------\n")
    print("Starting backend...")
    os.chdir(root_dir)
    os.system('START /B uvicorn MMP:app --reload')
    print("Backend started successfully.")
    print_process_info(os.getpid())
    print("----------------------------------------------------------------\n")


def stop_frontend():
    if not check_frontend_running():
        print("Frontend is not running")
        return
    print("----------------------------------------------------------------\n")
    print("Stopping frontend...")
    os.system('taskkill /F /IM node.exe')
    print("Frontend stopped successfully.")
    print("----------------------------------------------------------------\n")


def stop_backend():
    if not check_backend_running():
        print("Backend is not running")
        return
    print("----------------------------------------------------------------\n")
    print("Stopping backend...")
    os.system('taskkill /F /IM uvicorn.exe')
    print("Backend stopped successfully.")
    print("----------------------------------------------------------------\n")


def restart_frontend():
    print("----------------------------------------------------------------\n")
    print("Restarting frontend...")
    stop_frontend()
    start_frontend()
    print("Frontend restarted successfully.")
    print("----------------------------------------------------------------\n")


def restart_backend():
    print("----------------------------------------------------------------\n")
    print("Restarting backend...")
    stop_backend()
    start_backend()
    print("Backend restarted successfully.")
    print("----------------------------------------------------------------\n")


if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            print("----------------------------------------------------------------")
            print("Error: Invalid number of arguments.")
            print("Usage: ControlApp <command> <package>")
            print("Commands:")
            print("  --start frontend - Start the frontend")
            print("  --start backend - Start the backend")
            print("  --stop frontend - Stop the frontend")
            print("  --stop backend - Stop the backend")
            print("  --restart frontend - Restart the frontend")
            print("  --restart backend - Restart the backend")
            print("  --status frontend - Check frontend status")
            print("  --status backend - Check backend status")
            print("----------------------------------------------------------------")
            sys.exit()

        command = sys.argv[1]
        package = sys.argv[2]

        if command == '--start' and package == 'frontend':
            start_frontend()
            sys.exit()
        elif command == '--start' and package == 'backend':
            start_backend()
            sys.exit()
        elif command == '--start' and package == 'all':
            start_backend()
            start_frontend()
            sys.exit()
        elif command == '--stop' and package == 'frontend':
            stop_frontend()
            sys.exit()
        elif command == '--stop' and package == 'backend':
            stop_backend()
            sys.exit()
        elif command == '--stop' and package == 'all':
            stop_backend()
            stop_frontend()
            sys.exit()
        elif command == '--restart' and package == 'frontend':
            restart_frontend()
            sys.exit()
        elif command == '--restart' and package == 'backend':
            restart_backend()
            sys.exit()
        elif command == '--restart' and package == 'all':
            restart_backend()
            restart_frontend()
            sys.exit()
        elif command == '--status' and package == 'frontend':
            print("Frontend is running" if check_frontend_running() else "Frontend is not running")
            sys.exit()
        elif command == '--status' and package == 'backend':
            print("Backend is running" if check_backend_running() else "Backend is not running")
            sys.exit()
        elif command == '--status' and package == 'all':
            print("Frontend is running" if check_frontend_running() else "Frontend is not running")
            print("Backend is running" if check_backend_running() else "Backend is not running")
            sys.exit()
        else:
            print("Invalid command or package")
            sys.exit(1)
    except KeyboardInterrupt:
        print("----------------------------------------------------------------\n")
        print("Exiting...")
        print("----------------------------------------------------------------\n")
    except Exception as e:
        print("----------------------------------------------------------------\n")
        print(f"Error: {e}")
