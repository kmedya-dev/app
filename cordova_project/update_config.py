import os
from bs4 import BeautifulSoup

# These will be set by the GitHub Actions workflow
version_name = os.environ['VERSION_NAME']
version_code = os.environ['VERSION_CODE']
config_path = os.path.join('cordova_project', 'config.xml')

with open(config_path, 'r+') as f:
    soup = BeautifulSoup(f.read(), 'xml')
    
    widget = soup.find('widget')
    if not widget:
        raise ValueError("Could not find <widget> tag in config.xml")

    # Update version info
    widget['version'] = version_name
    widget['android-versionCode'] = version_code
    
    # Remove any existing icon tags to prevent duplicates
    for icon_tag in widget.find_all('icon'):
        icon_tag.decompose()

    # Add the new icon tag
    new_icon_tag = soup.new_tag('icon', src='res/icon/android/icon-512x512.png')
    widget.append(new_icon_tag)
    
    # Write the changes back to the file
    f.seek(0)
    f.write(str(soup))
    f.truncate()

print(f"Successfully updated {config_path} to version {version_name} ({version_code})")
