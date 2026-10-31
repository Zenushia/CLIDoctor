import sys
import datetime

ERROR_DATABASE = {
    "command not found": {
        "title": "Command Not Found / Path Issue",
        "cause": "The system cannot find the command or executable you entered.",
        "solution": "1. Check for typos.\n2. Ensure the program is installed.\n3. Add the program directory to your Windows Environment Variables (PATH)."
    },
    "access is denied": {
        "title": "Permission Error (Access Denied)",
        "cause": "Windows Terminal does not have sufficient admin privileges to execute this task.",
        "solution": "Close Windows Terminal and re-open it by right-clicking and selecting 'Run as Administrator'."
    },
    "syntaxerror": {
        "title": "Python Syntax Error",
        "cause": "There is a typo, missing parenthesis, or invalid keyword in your Python script.",
        "solution": "Open your script in a text editor and check the exact line mentioned in the error traceback."
    },
    "modulenotfounderror": {
        "title": "Missing Python Module",
        "cause": "The Python package you are trying to import is not installed in your environment.",
        "solution": "Run 'pip install <module_name>' in your Windows Terminal."
    },
    "execution of scripts is disabled": {
        "title": "PowerShell Script Execution Policy Error",
        "cause": "Windows restricts running custom PowerShell scripts by default for security.",
        "solution": "Run Windows Terminal as Admin and execute:\nSet-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
    }
}

def analyze_error(user_error):
    print("=" * 60)
    print(" 🩺 CLIDoctor - Windows Terminal Error Diagnostic Tool")
    print("=" * 60)
    print(f"⏰ Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📥 Input Error: \"{user_error}\"\n")

    matched = False
    for key, data in ERROR_DATABASE.items():
        if key in user_error.lower():
            matched = True
            print(f"🔍 Diagnosis       : {data['title']}")
            print(f"❓ Likely Cause    : {data['cause']}")
            print(f"💡 Prescription    :\n{data['solution']}")
            break

    if not matched:
        print("🔍 Diagnosis       : Generic / Unrecognized CLI Error")
        print("❓ Likely Cause    : Custom script error or unindexed system response.")
        print("💡 Prescription    : ")
        print("1. Check spelling and syntax.")
        print("2. Verify script paths and user permissions.")
        print("3. Query the log on StackOverflow or GitHub Issues.")

    print("=" * 60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py \"<Paste your Windows Terminal error here>\"")
    else:
        error_input = " ".join(sys.argv[1:])
        analyze_error(error_input)
