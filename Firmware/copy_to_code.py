import os
import shutil
import time
import subprocess
import platform

def is_circuitpython_device_connected():
    """Check if a CircuitPython device is connected"""
    system = platform.system()
    
    if system == "Windows":
        # Check for CircuitPython drives on Windows
        import string
        for drive in string.ascii_uppercase:
            drive_path = f"{drive}:\\"
            if os.path.exists(drive_path):
                try:
                    # Check if it's a CircuitPython device
                    if os.path.exists(os.path.join(drive_path, "boot_out.txt")):
                        return drive_path
                except:
                    continue
    elif system == "Darwin":  # macOS
        # Check for CircuitPython drives on macOS
        for i in range(10):
            drive_path = f"/Volumes/CIRCUITPY{i}"
            if os.path.exists(drive_path):
                return drive_path
        # Also check for the default CIRCUITPY volume
        if os.path.exists("/Volumes/CIRCUITPY"):
            return "/Volumes/CIRCUITPY"
    else:  # Linux
        # Check for CircuitPython drives on Linux
        for i in range(10):
            drive_path = f"/media/{os.getenv('USER', 'user')}/CIRCUITPY{i}"
            if os.path.exists(drive_path):
                return drive_path
        # Also check common mount points
        for path in ["/media/CIRCUITPY", "/mnt/CIRCUITPY"]:
            if os.path.exists(path):
                return path
    
    return None

def copy_main_to_code(device_path):
    """Copy main.py to code.py on the CircuitPython device"""
    main_file = "sojo.py"
    code_file = os.path.join(device_path, "code.py")
    
    if os.path.exists(main_file):
        try:
            shutil.copy2(main_file, code_file)
            print(f"✅ Successfully copied {main_file} to {code_file}")
            return True
        except Exception as e:
            print(f"❌ Error copying file: {e}")
            return False
    else:
        print(f"❌ {main_file} not found in current directory")
        return False

def main():
    print("🔍 Monitoring for CircuitPython devices...")
    print("Press Ctrl+C to stop")
    
    last_device = None
    
    while True:
        try:
            device_path = is_circuitpython_device_connected()
            
            if device_path and device_path != last_device:
                print(f"📱 CircuitPython device detected at: {device_path}")
                
                # Check if main.py exists in current directory
                if os.path.exists("main.py"):
                    print("📋 Copying main.py to code.py...")
                    if copy_main_to_code(device_path):
                        print("🎉 Keyboard firmware deployed successfully!")
                        print("💡 The device will now run the keyboard firmware on boot")
                    else:
                        print("⚠️  Failed to copy firmware")
                else:
                    print("❌ main.py not found in current directory")
                
                last_device = device_path
            elif not device_path and last_device:
                print("📱 CircuitPython device disconnected")
                last_device = None
            
            time.sleep(1)  # Check every second
            
        except KeyboardInterrupt:
            print("\n👋 Monitoring stopped")
            break
        except Exception as e:
            print(f"⚠️  Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main() 