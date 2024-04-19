import os
import platform
import sqlite3

def get_browser_cookie_path(browser_name):
    # Dictionary mapping browser names to their cookie file paths
    cookie_paths = {
    'Chrome': {
        'Windows': os.path.join(os.getenv('LOCALAPPDATA'), 'Google','Chrome','User Data','Profile 1','Network', 'Cookies'),
    },
    'Firefox': {
        'Windows': os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles', 'default', 'cookies.sqlite'),
        'Linux': os.path.expanduser('~/.mozilla/firefox/*.default/cookies.sqlite'),
        'Darwin': os.path.expanduser('~/.mozilla/firefox/*.default/cookies.sqlite')
    },
    # Add more browsers and their paths as needed
    }


    # Check if the specified browser and operating system are supported
    if browser_name in cookie_paths:
        if platform.system() in cookie_paths[browser_name]:
            return cookie_paths[browser_name][platform.system()]

    print("Unsupported browser or operating system")
    return None

def analyze_browser_cookies(browser_name):
    # Get the cookie file path for the specified browser
    cookie_path = get_browser_cookie_path(browser_name)
    if not cookie_path:
        return

    # Check if the database file exists
    if not os.path.exists(cookie_path):
        print("Database file not found:", cookie_path)
        return

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(cookie_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return

    # Query to select cookies from the database (modify as needed for different browsers)
    query = "SELECT name, value, host_key, path, expires_utc, is_secure FROM cookies"

    # Execute the query and fetch the results
    try:
        cursor.execute(query)
        cookies = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error executing the query:", e)
        conn.close()
        return

    # Print out the cookie information
    print("Found {} cookies in the {} browser:".format(len(cookies), browser_name))
    for cookie in cookies:
        name, value, host, path, expires, is_secure = cookie
        print("Name:", name)
        print("Value:", value)
        print("Host:", host)
        print("Path:", path)
        print("Expires:", expires)
        print("Secure:", bool(is_secure))
        print("-" * 30)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    print("Starting browser cookie analysis tool...")
    browser_name = input("Enter the name of the browser (e.g., Firefox, Chrome): ").strip()
    analyze_browser_cookies(browser_name)